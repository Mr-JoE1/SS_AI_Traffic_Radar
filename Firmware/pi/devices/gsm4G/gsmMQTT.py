'''
@Author : infinity tech ltd http://infinitytech.ltd/
@date   : 30 Aug 2023
@file   : gsmMQTT.py
@brief  : this code will be responsible for all low level MQTT Communication 


////todo: make the mqtt.json parsing here

'''



from datetime import datetime
import sys



new_path = '../../utils'
sys.path.append(new_path)

from Loggoer import Logger
from gsmCore import GsmCore

mylog=Logger("gsmMQTT: ")



ERR = '\033[91m'
SUCCESS = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset text attributes to normal


def dbg(status=RESET, msg=""):
    current_time_ms = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    mylog.Log(str(current_time_ms)+"  :"+msg)
    # if (status == RESET):
        # print(str(current_time_ms)+"  gsmCore:"+msg+" \n")
    # else:
        # print(status, str(current_time_ms)+"  gsmCore:"+msg+"\n")





class GsmMQTT(GsmCore):
    def __init__(self):
        super().__init__()



    '''
    Configure the MQTT protocol version

    '''
    def setVersion(self,client_idx,vsn):
        res = self.wrATCMD("AT+QMTCFG",["version",client_idx,vsn])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't set MQTT Version...")

    ##############################################################

    '''
    Configure the PDP to be used by the MQTT client
    '''
    def setPDP(self,client_idx,cid):
        res = self.wrATCMD("AT+QMTCFG",["pdpcid",client_idx,cid])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't set MQTT PDP ...")

    ################################################################

    '''
    Configure Will information
    '''
    def setWillInfo(self,client_idx,will_fg,will_qos,will_retain,will_topic,will_msg):
        res = self.wrATCMD("AT+QMTCFG",["will",client_idx,will_fg,will_qos,will_retain,will_topic,will_msg])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't set MQTT will ...")  


    ################################################################

    '''
    Configure timeout of message delivery
    '''
    def setTimeOut(self,client_idx,pkt_timeout,retry_times,timeout_notice):
        res = self.wrATCMD("AT+QMTCFG",["timeout",client_idx,pkt_timeout,retry_times,timeout_notice])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't set MQTT timeout ...")  

    ################################################################

    '''
    Configure the session type
    '''
    def setSession(self,client_idx,clean_session):
        res = self.wrATCMD("AT+QMTCFG",["session",client_idx,clean_session])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't set MQTT session Type ...")  


    ################################################################

    '''
    Configure the keep-alive time
    '''
    def setKeepAliveTime(self,client_idx,keep_alive_time):
        res = self.wrATCMD("AT+QMTCFG",["keepalive",client_idx,keep_alive_time])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't set MQTT KeepAliveTime  ...")  


    ################################################################

    '''
    Configure the MQTT SSL mode and SSL context index   
    '''
    def setSSL(self,client_idx,SSL_enable,SSL_ctx_idx):
        res = self.wrATCMD("AT+QMTCFG",["ssl",client_idx,SSL_enable,SSL_ctx_idx])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't set MQTT SSL ...")  


    ################################################################
    
    '''
    Configure receiving mode when data is received from server
    '''
    def setRecivingMode(self,client_idx,msg_recv_mode,msg_len_enable):
        res = self.wrATCMD("AT+QMTCFG",["recv/mode",client_idx,msg_recv_mode,msg_len_enable])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't set MQTT receiving mode ...")  


    ################################################################

    '''
    Configure receiving mode when data is received from server
    '''
    def setRecivingMode(self,client_idx,msg_recv_mode,msg_len_enable):
        res = self.wrATCMD("AT+QMTCFG",["recv/mode",client_idx,msg_recv_mode,msg_len_enable])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't Configure receiving mode when data is received from server ...")  

    ################################################################

    '''
    Configure Alibaba device information for Alibaba Cloud
    '''
    def setAlibabaInfo(self,client_idx,product_key,device_name,device_secret):
        res = self.wrATCMD("AT+QMTCFG",["aliauth",client_idx,product_key,device_name,device_secret])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn'tConfigure Alibaba device information for Alibaba Cloud...")      

    ################################################################

    '''
    Configure the MQTT heartbeat interval
    '''
    def setHeartBeatInterval(self,client_idx,qmtping_interval):
        res = self.wrATCMD("AT+QMTCFG",["qmtping",client_idx,qmtping_interval])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't set MQTT receiving mode ...")  

    ################################################################

    '''
    use this function to list the MQTT Network range of supported <client_idx>s ,host_
    name and (range of supported <port>s)
    '''    
    def listNetwor(self):
        res= self.testATCMD("AT+QMTOPEN")
        if(res.status == True):
            out=str(res.body).replace("OK","").replace("+QMTOPEN:","").split(",")
            try:
                clientIDXs=out[0]
                hostName=out[1]
                ports=out[2]
                return clientIDXs,hostName,ports
            except:
                dbg("couldn't list MQTT Network ......")
        else:
                dbg("couldn't list MQTT Network ......")

        return "","",""

    ##################################################################

    '''
    use this function to get the oppened network 
    '''
    def getOppenedNetwork(self):
        res=self.readATCMD("AT+QMTOPEN")
        if(res.status ==True):
            try:
                out=str(res.body).replace("OK","").replace("[+QMTOPEN:","").replace("]","").split(",")
                clientIdx=out[0]
                hostName=out[1]
                port=out[2]
                return clientIdx,hostName,port
            except:
                dbg("failed to get the oppened network .....")
        else:
                dbg("failed to get the oppened network .....")
        return "","",""
    
    ##################################################################
    
    '''
    use this function to open MQTT network
    -1  Failed to open network
    0   Network opened successfully
    1   Wrong parameter
    2   MQTT identifier is occupied
    3   Failed to activate PDP
    4   Failed to parse domain name
    5   Network connection error
    '''
    def open(self,client_idx,host_name,port):  
        res=self.wrATCMD("AT+QMTOPEN",[client_idx,host_name,port])
        if(res.status==True):
            out = str(res.body).replace("OK", "").replace("+QMTOPEN:","").replace(client_idx,"").replace(",","").replace(" ", "")
            state=""
            if   (int(out)== -1) :  state = "Failed to open network"
            elif (int(out)== 0)  :  state = "Network opened successfully"
            elif (int(out)== 1)  :  state = "Wrong parameter"
            elif (int(out)== 2)  :  state = "MQTT identifier is occupied"
            elif (int(out)== 3)  :  state = "Failed to activate PDP"
            elif (int(out)== 4)  :  state = "Failed to parse domain name"
            else                 :  state = "Network connection error"
            dbg(state)
            print(state)
            return state   
        else :
            print("error couldn't open MQTT Network .....")
            dbg("error couldn't open MQTT Network .....")  

    ##################################################################
    
    '''
    use this member function to close MQTT network 
    -1  Failed to close network
     0  Network closed successfully
    '''
    def close(self,client_idx):
        res=self.write("AT+QMTCLOSE",[client_idx])
        if(res.status==True):
            out = str(res.body).replace("OK", "").replace("+QMTCLOSE:","").replace(client_idx,"").replace(",","").replace(" ", "")
            state=""
            if(int(out)== 0):  state = "Network closed successfully"
            else            :  state = "Failed to close network"
            dbg(state)
            return state
        else :
            print("error couldn't close MQTT Network .....")
            dbg("error couldn't close MQTT Network .....")    

    ##################################################################


    '''
    This function connects a client to MQTT server. When a TCP/IP socket connection is established from a
    client to a server, a protocol level session must be created using a CONNECT flow.
    
    result
        0   Packet sent successfully and ACK received from server
        1   Packet retransmission
        2   Failed to send packet
    ret_code
        0   Connection Accepted
        1   Connection Refused: Unacceptable Protocol Version
        2   Connection Refused: Identifier Rejected
        3   Connection Refused: Server Unavailable
        4   Connection Refused: Bad User Name or Password
        5   Connection Refused: Not Authorized    
    ''' 
    def connect(self,client_idx,client_id,username,password):
        res=self.wrATCMD("AT+QMTCONN",[client_idx,client_id,username,password])
        if(res.status==True):
            try:
                out = str(res.body).replace("OK", "").replace("+QMTCONN:","").replace(client_idx,"").replace(",","").replace(" ", "").replace("[","#").replace("]","").split("#")
                result=int(out[0])
                retCode=int(out[1])
                dbg("Mqtt connection return result= "+out[0]+"ret_code"+out[1])
                return result,retCode
            except: 
                print("mqtt failed to connect......")
                dbg("mqtt failed to connect......")
        else:
                print("mqtt failed to connect......")
                dbg("mqtt failed to connect......")

    ##################################################################

    '''
    use this member function to close MQTT network 
    -1  Failed to connection network
     0  Network disconnection successfully
    '''
    def disconnect(self,client_idx):
        res=self.write("AT+QMTDISC",[client_idx])
        if(res.status==True):
            out = str(res.body).replace("OK", "").replace("+QMTDISC:","").replace(client_idx,"").replace(",","").replace(" ", "")
            state=""
            if(int(out)== 0):  state = "Network closed successfully"
            else            :  state = "Failed to close network"
            dbg(state)
            return state
        else :
            print("error couldn't close MQTT Network .....")
            dbg("error couldn't close MQTT Network .....")    

    ##################################################################

    '''
    This command subscribes to one or more topics. A SUBSCRIBE message is sent by a client to register an
    interest in one or more topic names with the server. Messages published to these topics are delivered
    from the server to the client as PUBLISH messages

    client_idx>,<msgid>,"<topic1>",<qos1>[,"<topic2>",<qo

    Integer type. The QoS level at which the client wants to publish the messages.
        0   At most once
        1   At least once
        2   Exactly once
    
        result
        0   Sent packet successfully and received ACK from server
        1   Packet retransmission
        2   Failed to send packet

    '''
    def subscribe(self,client_idx,msgId,topic,qos):
        res=self.wrATCMD("AT+QMTSUB",[client_idx,msgId,topic,qos])
        if(res.status == True):
            out=str(res.body)
        else:
            print("failed to subscribe topic....."+topic)
            dbg("failed to subscribe topic"+topic)

    ##################################################################

    '''
    This command publishes messages with fixed length by a client to a server for distribution to interested
    subscribers. Each PUBLISH message is associated with a topic name. If a client subscribes to one or
    more topics, any message published to those topics will be sent by the server to the client as a PUBLISH
    message

    AT+QMTPUBEX=<client_idx>,<msgid>,<qos>,<retain>,"<topic>",<msg_length>
    '''
    def publish(self,client_idx,msgid,qos,retain,topic,msg_length,msg):
        res=self.wrATCMD("AT+QMTSUB",[client_idx,msgid,qos,retain,topic,msg_length])
        if(res.status == True):
            out=str(res.body)
            cmde = b'\r\n'
            cmdtosend = msg.encode('utf-8')+cmde
            self.ser.write(cmdtosend)  
        else:
            print("failed to publish to topic....."+topic)
            dbg("failed to publish to topic"+topic)

    ##################################################################
