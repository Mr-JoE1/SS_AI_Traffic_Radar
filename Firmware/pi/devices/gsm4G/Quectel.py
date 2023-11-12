'''
@Author : infinity tech ltd
@date   : 24 Sep 2023
@file   : Quectel.py
@brief  : this code will be responsible for handring AT commands 

'''


import json
from gsmCore import GsmCore
from datetime import datetime
from gsmGeneral import GsmGeneral
from gsmSerialInterfaceCtrl import GsmSerialInterfaceCTRL
from gsmNetwork import GsmNetwork
from gsmStatusControl import GsmStatusControl
from gsmMQTT import GsmMQTT


fileCfgFile="mqtt.json"



ERR = '\033[91m'
SUCCESS = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset text attributes to normal


def dbg(status=RESET, msg=""):
    current_time_ms = datetime.now().strftime("%H:%M:%S:%f")[:-3]
    if (status == RESET):
        print(str(current_time_ms)+"  gsmStatusControl:"+msg+" \n")
    else:
        print(status, str(current_time_ms)+"  gsmStatusControl:"+msg+"\n")




class Quectel:

    '''
        Guiedlines on how to initialize your device for lte data access only
        reference : https://www.twilio.com/docs/iot/supersim/cellular-modem-knowledge-base#module-specific-details
        
            1- config your APN
            2- Disable 2G (GSM)
            3- Data-centric attach mode
            4- Configure the URC UART
            5- ping 8.8.8.8
    '''

    def __init__(self):
            self.gsm=GsmCore()
            res = self.gsm.wrATCMD("AT+CGDCONT",[1,"IP","super"])
            print("1-APN Configig : "+str(res.body)+"\n")
            res = self.gsm.wrATCMD("AT+QCFG",["nwscanmode",3])
            print("2-disable 2G (GSM) : "+str(res.body)+"\n")
            res = self.gsm.wrATCMD("AT+QCFG",["servicedomain",1])
            print("3-Data-centric attach mode : "+str(res.body)+"\n")
            res = self.gsm.wrATCMD("AT+QURCCFG",["urcport","uart1"])
            print("4- Configure the URC UART : "+str(res.body)+"\n")
            res = self.gsm.wrATCMD("AT+QPING",[1,"8.8.8.8"])
            print("5- ping 8.8.8.8 : "+str(res.body)+"\n")
    


    '''
    mqtt config

    1- configure the mqtt reciving mode
    2- open the network


    '''
    def initMQTT(self):
        with open('/etc/SS/gsm/mqtt.json', 'r') as file:    
            self.content = json.load(fileCfgFile)
            print(str(self.content))
            self.mqtt=GsmMQTT()
            self.mqtt.setRecivingMode(str(self.content["client_idx"]),0,1)
            print("mqtt init.open: "+str(self.mqtt.open(self.content["client_idx"],self.content["broker_address"],self.content["port"])+'\n'))
            self.msgID=0
            # print("available topics are: "+self.mqtt)


        
    '''
    for now will print the incomming topic message
    '''
    def mqttSubscribe(self,topic):
        self.msgID=self.msgID+1
        self.mqtt.subscribe(self.content["client_idx"],self.msgID,topic,self.content["qos"])
    


    '''
    will publish message to a broker and subscriber
    '''
    def mqttpublish(self,topic,msg):
        self.msgID=self.msgID+1
        self.mqtt.publish(self.content["client_idx"],self.msgID,self.content["qos"],self.content["retain"],topic,str(msg).len,msg)