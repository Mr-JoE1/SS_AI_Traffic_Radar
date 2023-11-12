'''
@Author : infinity tech ltd
@date   : 31 Aug 2023
@file   : gsmSerialInterfaceCtrl.py
@brief  : this code will be responsible for handring AT commands 

'''


from gsmCore import GsmCore
from datetime import datetime

ERR = '\033[91m'
SUCCESS = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset text attributes to normal


def dbg(status=RESET, msg=""):
    current_time_ms = datetime.now().strftime("%H:%M:%S:%f")[:-3]
    if (status == RESET):
        print(str(current_time_ms)+"  gsmSerialInterfaceCTRL:"+msg+" \n")
    else:
        print(status, str(current_time_ms)+"  gsmSerialInterfaceCTRL:"+msg+"\n")


class GsmSerialInterfaceCTRL(GsmCore):
    def __init__(self):
        super.__init__()


    '''
    This command controls the behavior of the UE’s DCD (data carrier detection) line.
    '''
    def setDCDFunctionMode(self,value):
        cmd="AT&C"+str(value)
        res=self.execATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute")

    '''
    This command determines how the UE responds if DTR line is changed from low to high level during data
    '''
    def  setDTRFunctionMode(self,value):
        cmd="AT&D"+str(value)    
        res=self.execATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute")


    '''
    This command determines the flow control behavior of the serial port for data mode.
    '''        
    def setTE_TALocalDataFlowControl_test(self):
        res=self.testATCMD("AT+IFC")
        if(res.status!=True):
            dbg("failed to execute")
        return res.body

    '''
    This command determines the flow control behavior of the serial port for data mode.
    '''        
    def setTE_TALocalDataFlowControl_read(self): 
        res=self.readATCMD("AT+IFC")
        if(res.status!=True):
            dbg("failed to execute")
        return res.body
    
    '''
    This command determines the flow control behavior of the serial port for data mode.
    '''        
    def setTE_TALocalDataFlowControl_write(self,dce,dte): 
        res=self.wrATCMD("AT+IFC",[dce,dte])
        if(res.status!=True):
            dbg("failed to execute")
        # return res.body    

    '''
    This command determines the serial interface character framing format and parity received by TA from
    TE.
    '''  
    def setTE_TAControlCharacterFraming_test(self):
        res=self.testATCMD("AT+ICF")  
        if(res.status!=True):
            dbg("failed to execute")
        return res.body   

    '''
    This command determines the serial interface character framing format and parity received by TA from
    TE.
    '''  
    def setTE_TAControlCharacterFraming_read(self):
        res=self.readATCMD("AT+IFC")
        if(res.status!=True):
            dbg("failed to execute")
        return res.body 
    

    '''
    This command determines the flow control behavior of the serial port for data mode.
    '''        
    def setTE_TALocalDataFlowControl_write(self,format,parity): 
        res=self.wrATCMD("AT+IFC",[format,parity])
        if(res.status!=True):
            dbg("failed to execute")


    '''
    This command queries and set the baud rate of the UART.
    ''' 
    def setTE_TAFixedLocalRate_test(self):
        res=self.testATCMD("AT+IPR")
        if(res.status!=True):
            dbg("failed to execute")
        return res.body        


    '''
    This command queries and set the baud rate of the UART.
    ''' 
    def setTETAFixedLocalRate_read(self):
        res=self.readATCMD("AT+IPR")
        if(res.status!=True):
            dbg("failed to execute")
        return res.body     


    '''
    This command queries and set the baud rate of the UART.
    '''   
    def setTETAFixedLocalRate_write(self,rate):
        res=self.wrATCMD("AT+IPR",[rate])
        if(res.status!=True):
            dbg("failed to execute")           


    '''
    This command restores RI behavior to inactive.
    '''
    def restoreRIBehaviortoInactive_test(self):
        res=self.testATCMD("AT+QRIR")
        if(res.status!=True):
            dbg("failed to execute")
        return res.body        


    '''
    This command restores RI behavior to inactive.
    '''
    def restoreRIBehaviortoInactive_exec(self):
        res=self.execATCMD("AT+QRIR")
        if(res.status!=True):
            dbg("failed to execute")
        return res.body   