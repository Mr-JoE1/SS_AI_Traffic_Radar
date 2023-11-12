'''
@Author : infinity tech ltd http://infinitytech.ltd/
@date   : 30 Aug 2023
@file   : gsmGeneral.py
@brief  : this code will be responsible for handring AT commands 

'''


from gsmCore import GsmCore
from datetime import datetime


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
    current_time_ms = datetime.now().strftime("%H:%M:%S:%f")[:-3]
    if (status == RESET):
        print(str(current_time_ms)+"  gsmGeneral:"+msg+" \n")
    else:
        print(status, str(current_time_ms)+"  gsmGeneral:"+msg+"\n")


class GsmGeneral(GsmCore):

    def __init__(self):
       super().__init__()

    '''
    Display MT Identification Information
    '''
    def displayMTIdentificationInfo(self):
        res = self.execATCMD("ATI")
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't complete request...")

    '''
    Request Manufacturer Identification
    '''
    def requestManufacturerID(self):
        res = self.testATCMD("AT+GMI")
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't complete request...")

    '''
    Request Model Identification
    '''
    def requestModelIdentification(self):
        res = self.testATCMD("AT+GMM")
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't complete request...")

    '''
    Request TA Firmware Revision Identification
    '''
    def requestTAFirmwareRevision(self):
        res = self.testATCMD("AT+GMR")
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't complete request...")

    '''
    This command requests the International Mobile Equipment Identity (IMEI) number which permits the
    user to identify individual ME device and the Serial Number (SN) of the ME.
    '''
    def requestIMEIandSN_test(self):
        res = self.testATCMD("AT+GSN")
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't complete request...")

    '''
    This command requests the International Mobile Equipment Identity (IMEI) number which permits the
    user to identify individual ME device and the Serial Number (SN) of the ME.
    '''
    def requestIMEIandSN_write(self, snt):
        res = self.wrATCMD("AT+GSN", [snt])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't complete request...")

    '''
    This command requests the International Mobile Equipment Identity (IMEI) number which permits the
    user to identify individual ME device and the Serial Number (SN) of the ME.
    '''
    def requestIMEIandSN_exec(self):
        res = self.execATCMD("AT+GSN")
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            # return out
        else:
            dbg("error couldn't complete request...")

    '''
    his Execution command requests the International Mobile Equipment Identity (IMEI) number which
    permits the user to identify individual ME device and the Serial Number (SN) of the ME.
    '''
    def requestIMEI_test(self):
        res = self.testATCMD("AT+CGSN")
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't complete request...")

    '''
    his Execution command requests the International Mobile Equipment Identity (IMEI) number which
    permits the user to identify individual ME device and the Serial Number (SN) of the ME.
    '''
    def requestIMEI_write(self, snt):
        res = self.wrATCMD("AT+CGSN", [snt])
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            return out
        else:
            dbg("error couldn't complete request...")

    '''
    his Execution command requests the International Mobile Equipment Identity (IMEI) number which
    permits the user to identify individual ME device and the Serial Number (SN) of the ME.
    '''
    def requestIMEI_exec(self):
        res = self.execATCMD("AT+CGSN")
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            # return out
        else:
            dbg("error couldn't complete request...")

    '''
    This command resets AT command settings to the default values specified by the manufacturer.
    '''
    def resetATCommandSetting(self):
        res = self.execATCMD("AT&F0")
        if (res.status != True):
            dbg("error couldn't complete request...")

    '''
    This command displays the current settings of several AT command parameters
    '''
    def displayCurrentConfigurations(self):
        res = self.execATCMD("AT&V")
        if (res.status == True):
            out = str(res.body).replace("OK", "")
            print(out)
            # return out
        else:
            dbg("error couldn't complete request...")

    '''
    This command stores the current AT command settings to a user-defined profile in non-volatile memory.
    '''
    def storeCurrentUserProfile(self, profileNumber):
        res = self.execATCMD("AT&W"+str(profileNumber))
        if (res.status != True):
            dbg("error couldn't complete request...")

    '''
    This command first resets the AT command settings to their manufacturer defaults. Afterwards, the AT
    command settings are restored from the user-defined profile in the non-volatile memory, if they have been
    stored with AT&W before
    '''
    def setCurrParamstoUserProfile(self,value):
        res = self.execATCMD("ATZ"+str(value))
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command controls whether the result code is transmitted to the TE. Other information text
    transmitted as response is not affected.
    '''
    def setResultCodePresentationMode(self,n):
        res = self.execATCMD("ATQ"+str(n))
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command determines the contents of header and trailer transmitted with AT command result codes
    and information responses
    '''
    def setMTResponseFormat(self,value):
        res = self.execATCMD("ATV"+str(value))
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command controls whether TA echoes characters received from TE or not during AT command
    mode.
    '''
    def setCommandEchoMode(self,value):
        res = self.execATCMD("ATE"+str(value))
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command repeats previous AT command line, and "/" acts as the line terminating character
    '''
    def repet(self):
        res = self.execATCMD("A/")
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command determines the character recognized by TA to terminate an incoming command line. It is
    also generated for result codes and information text, along with character value set via ATS4.
    '''
    def setCommandLineTerminationCharacter_read(self):
        res=self.readATCMD("ATS3")
        if (res.status != True):
            dbg("error couldn't complete request...")
        else:
            return str(res.body).replace("OK","")     
        


    '''
    This command determines the character recognized by TA to terminate an incoming command line. It is
    also generated for result codes and information text, along with character value set via ATS4.
    '''
    def setCommandLineTerminationCharacter_write(self,n):
        res=self.wrATCMD("ATS3",[n])
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command determines the character generated by TA for result code and information text, along with
    the command line termination character set via ATS3.
    '''                
    def setResponseFormattingCharacter_read(self):
        res=self.readATCMD("ATS4")
        if (res.status != True):
            dbg("error couldn't complete request...")
        else:
            return str(res.body).replace("OK","")     
        

    '''
    This command determines the character generated by TA for result code and information text, along with
    the command line termination character set via ATS3.
    '''                
    def setResponseFormattingCharacter_write(self,n):
        res=self.wrATCMD("ATS4",n)
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command determines the character value used by the module to delete the immediately preceding
    character from the AT command line (i.e. equates to backspace key).
    '''
    def setCommandLineEaditingCharacter_read(self):
        res=self.readATCMD("ATS5")
        if (res.status != True):
            dbg("error couldn't complete request...")
        else:
            return str(res.body).replace("OK","")     
      

    '''
    This command determines the character value used by the module to delete the immediately preceding
    character from the AT command line (i.e. equates to backspace key).
    '''
    def setCommandLineEaditingCharacter_write(self,n):
        res=self.wrATCMD("ATS5",n)
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command determines whether TA transmits particular result codes to the TE or not. It also controls
    whether TA detects the presence of a dial tone when it begins dialing and the engaged tone (busy signal)
    or not.
    '''
    def setConnectedResultCodeFormat(self,value):
        res=self.execATCMD("ATX"+str(value))
        if (res.status != True):
            dbg("error couldn't complete request...")
 

    '''
    This command controls the functionality level. It can also be used to reset the UE.
    '''
    def setUEFunctionality_test(self):
        res=self.testATCMD("AT+CFUN")
        if (res.status != True):
            dbg("error couldn't complete request...")
 

    '''
    This command controls the functionality level. It can also be used to reset the UE.
    '''
    def setUEFunctionality_read(self):
        res=self.readATCMD("AT+CFUN")
        if (res.status != True):
            dbg("error couldn't complete request...")
        return str(res.body).replace("OK","")
    
   
    '''
    This command controls the functionality level. It can also be used to reset the UE.
    '''
    def setUEFunctionality_write(self,fun,rst):
        res=self.wrATCMD("AT+CFUN",[fun,rst])
        if (res.status != True):
            dbg("error couldn't complete request...")
    
    
    '''
    This command controls the format of error result codes: ERROR, error numbers or verbose messages as
    +CME ERROR: <err> and +CMS ERROR: <err>. This command disables or enables the use of final
    result code +CME ERROR: <err> as the indication of an error.
    '''
    def errorMessageFormat_test(self):
        res=self.testATCMD("AT+CMEE")
        if (res.status != True):
            dbg("error couldn't complete request...")

    '''
    This command controls the format of error result codes: ERROR, error numbers or verbose messages as
    +CME ERROR: <err> and +CMS ERROR: <err>. This command disables or enables the use of final
    result code +CME ERROR: <err> as the indication of an error.
    '''
    def errorMessageFormat_read(self):
        res=self.readATCMD("AT+CMEE")
        if (res.status != True):
            dbg("error couldn't complete request...")
        return str(res.body).replace("OK","")
    


    '''
    This command controls the format of error result codes: ERROR, error numbers or verbose messages as
    +CME ERROR: <err> and +CMS ERROR: <err>. This command disables or enables the use of final
    result code +CME ERROR: <err> as the indication of an error.
    '''
    def errorMessageFormat_write(self,n):
        res=self.wrATCMD("AT+CMEE",[n])
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command informs the MT which character set is used by the TE. TA is then able to convert character
    strings correctly between TE and MT character sets.
    '''
    def selectTECharacterSet_test(self):
        res=self.testATCMD("AT+CSCS")
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command informs the MT which character set is used by the TE. TA is then able to convert character
    strings correctly between TE and MT character sets.
    '''
    def selectTECharacterSet_read(self):
        res=self.readATCMD("AT+CSCS")
        if (res.status != True):
            dbg("error couldn't complete request...")
        return str(res.body).replace("OK","")


    '''
    This command informs the MT which character set is used by the TE. TA is then able to convert character
    strings correctly between TE and MT character sets.
    '''
    def selectTECharacterSet_write(self,chset):
        res=self.wrATCMD("AT+CSCS",[chset])
        if (res.status != True):
            dbg("error couldn't complete request...")

    
    '''
    This commands configures the output port of URC.
    '''
    def configureURCIndicationOption_test(self):
        res=self.testATCMD("AT+QURCCFG")
        if (res.status != True):
            dbg("error couldn't complete request...")

    '''
    This commands configures the output port of URC.
    '''
    def configureURCIndicationOption_write(self,urcPort,urcPortValue):
        res=self.wrATCMD("AT+QURCCFG",[urcPort,urcPortValue])
        if (res.status != True):
            dbg("error couldn't complete request...")


    '''
    This command configures whether to enable the specified URC or not after the process of AP side were
    booted successfully
    '''
    def configureToReportSpecifiedURC_read(self):
        res=self.readATCMD("AT+QAPRDYIND")
        if (res.status != True):
            dbg("error couldn't complete request...")
        return str(res.body).replace("OK","")

    '''
    This command configures whether to enable the specified URC or not after the process of AP side were
    booted successfully
    '''
    def configureToReportSpecifiedURC_write(self,cfgVal):
        res=self.wrATCMD("AT+QURCCFG",[cfgVal])
        if (res.status != True):
            dbg("error couldn't complete request...")



    '''
    This commans configures debug UART as AT port.
    '''
    def debugUARTConfiguration_read(self):
        res=self.readATCMD("AT+QDIAGPORT")
        if (res.status != True):
            dbg("error couldn't complete request...")
        return str(res.body).replace("OK","")

    '''
    This commans configures debug UART as AT port.
    '''
    def debugUARTConfiguration_write(self,num):
        res=self.wrATCMD("AT+QDIAGPORT",[num])
        if (res.status != True):
            dbg("error couldn't complete request...")

