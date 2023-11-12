'''
@Author : infinity tech ltd http://infinitytech.ltd/
@date   : 28 Aug 2023
@file   : gsmCore.py
@brief  : this code will be responsible for handring AT commands 

'''

'''
logger : will  date-time.txt
each log take time , module , error/info and result 
timeSyncorinization : sync the time 
'''

import serial
import time
import json
from datetime import datetime
import os

import sys

new_path = '../../utils'
sys.path.append(new_path)

from Loggoer import Logger

mylog=Logger("gsmCore: ")

ERR = '\033[91m'
SUCCESS = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset text attributes to normal


def dbg(status=RESET, msg=""):
    current_time_ms = datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
    mylog.Log(str(current_time_ms)+"  :"+msg)
    # if (status == RESET):
        # print(str(current_time_ms)+"  gsmCore:"+msg+" \n")
    # else:
        # print(status, str(current_time_ms)+"  gsmCore:"+msg+"\n")


class GsmResponse:
    def __init__(s, st, res):
        s.status = st
        s.body = res


class GsmCore:
    def __init__(self):
        dbg("gsmCore\n")
        try:
            self.readConfiguration()
            dbg("gsm configuration file has been found......")

        except:
            dbg(ERR, "error code 1 , gsm config file not found!")
            dbg("generating default config file ......")
            os.system("sudo mkdir -p /etc/SS/gsm")
            os.system("sudo cp gsm.json /etc/SS/gsm/gsm.json")
            try:
                self.readConfiguration()
            except:
                dbg(ERR, "error code 2 , failed to create configuration file")

        # parity
        if (self.content["parity"] == "none"):
            self.prty = serial.PARITY_NONE
        elif (self.content["parity"] == "even"):
            self.prty = serial.PARITY_EVEN
        elif (self.content["parity"] == "odd"):
            self.prty = serial.PARITY_ODD
        else:
            dbg(ERR, "error code 3 , invalid parity setting check out your gsm.json")

        # stop bits
        if (self.content["stopbits"] == 1):
            self.stpbit = serial.STOPBITS_ONE
        elif (self.content["stopbits"] == 2):
            self.stpbit = serial.STOPBITS_TWO
        elif (self.content["stopbits"] == 5):
            self.stpbit = serial.STOPBITS_ONE_POINT_FIVE
        else:
            dbg(ERR, "error code 4 , invalid setting stopbit check out your gsm.json")

        # stop bits
        if (self.content["bytesize"] == 8):
            self.btsz = serial.EIGHTBITS
        elif (self.content["bytesize"] == 7):
            self.btsz = serial.SEVENBITS
        elif (self.content["bytesize"] == 6):
            self.btsz = serial.SIXBITS
        elif (self.content["bytesize"] == 5):
            self.btsz = serial.FIVEBITS
        else:
            dbg(ERR, "error code 5 , invalid setting bytesize check out your gsm.json")

        try:

            self.ser = serial.Serial(
                port=self.content["port"],
                baudrate=self.content["baudrate"],
                parity=self.prty,
                stopbits=self.stpbit,
                bytesize=self.btsz,
                timeout=self.content["timeout"]
            )
            self.ser.flush()
            # dbg(SUCCESS,"initialized serial port succesfuly")

        except Exception as e:
            if (os.path.exists(self.content["port"]) == False):
                dbg(ERR, "error code 7 , couldn't initialize the serial port make sure your gsm device is connected ")
            dbg(ERR, "failed for unknown"+str(e))

        dbg(str(self.ser.isOpen()))
        if (self.ser.isOpen() == True):
            dbg(SUCCESS, "initialized serial port succesfuly")
        else:
            dbg(ERR, "error code 8 ,couldn't initialize the serial port try chmod 777 /dev/portname")

    #########################################################

    def readConfiguration(self):
        with open('/etc/SS/gsm/gsm.json', 'r') as file:
            self.content = json.load(file)
            dbg("port:"+self.content["port"] +
                "\n,baudrate:"+str(self.content["baudrate"])+" \n"+self.content["parity"])

    #########################################################

    def execATCMD(self, cmd):
        try:
            cmde = b'\r\n'
            cmdtosend = cmd.encode('utf-8')+cmde
            self.ser.write(cmdtosend)
            time.sleep(0.4)               # wait for the response
            data = self.ser.readline()
            if (str(data).find("ERROR") > -1):
                dbg(ERR, "error code 9 , failed to execute , invalid command....")
                return GsmResponse(False, str(data))
            else:
                dbg("executed succesfully....")
                dbg(str(data))
                return GsmResponse(True, str(data))

        except Exception as e:
            dbg(ERR, "error code 10 , serial port hasn't been initialized....."+e)
            return GsmResponse(False, "")

    ###############################################################

    def testATCMD(self, cmd):
        try:
            cmde = b'=?\r\n'
            cmdSend = cmd.encode('utf-8') + cmde
            self.ser.write(cmdSend)
            time.sleep(0.4)
            data = self.ser.readline()
            if (str(data).find("ERROR") > -1):
                dbg(ERR, "error code 9 , failed to execute , invalid command....")
                return GsmResponse(False, str(data))
            else:
                dbg("executed succesfully....")
                dbg(str(data))
                return GsmResponse(True, str(data))
        except Exception as e:
            dbg(ERR, "error code 10 , serial port hasn't been initialized....."+e)
            return GsmResponse(False, "")

    ###############################################################

    def readATCMD(self, cmd):
        try:
            cmde = b'?\r\n'
            cmdSend = cmd.encode('utf-8') + cmde
            self.ser.write(cmdSend)
            time.sleep(0.4)
            data = self.ser.readline()
            if (str(data).find("ERROR") > -1):
                dbg(ERR, "error code 9 , failed to execute , invalid command....")
                return GsmResponse(False, str(data))
            else:
                dbg("executed succesfully....")
                dbg(str(data))
                return GsmResponse(True, str(data))
        except Exception as e:
            dbg(ERR, "error code 10 , serial port hasn't been initialized....."+e)
            return GsmResponse(False, "")

    ###############################################################

    def wrATCMD(self, cmd, params):
        try:
            cmde = b'='
            ctr = 0
            for item in params:
                if (type(item) == str):
                    ctr = ctr+1
                    if (ctr != 1):
                        cmde = cmde+b'[,'
                    cmde = cmde+item.encode('utf-8')
                else:
                    ctr = ctr+1
                    if (ctr != 1):
                        cmde = cmde+b'[,'
                    cmde = cmde+str(item).encode('utf-8')
            for i in range(ctr-1):
                cmde = cmde+b']'
            cmde = cmde+b'\r\n'
            cmdSend = cmd.encode('utf-8') + cmde
            self.ser.write(cmdSend)
            time.sleep(0.4)
            data = self.ser.readline()
            if (str(data).find("ERROR") > -1):
                dbg(ERR, "error code 9 , failed to execute , invalid command....")
                return GsmResponse(False, str(data))
            else:
                dbg("executed succesfully....")
                dbg(str(data))
                return GsmResponse(True, str(data))
        except Exception as e:
            dbg(ERR, "error code 10 , serial port hasn't been initialized....."+e)
            return GsmResponse(False, "")




         