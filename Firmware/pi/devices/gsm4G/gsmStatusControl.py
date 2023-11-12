'''
@Author : infinity tech ltd
@date   : 2 Aug 2023
@file   : gsmStatusControl.py
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
        print(str(current_time_ms)+"  gsmStatusControl:"+msg+" \n")
    else:
        print(status, str(current_time_ms)+"  gsmStatusControl:"+msg+"\n")








class GsmStatusControl(GsmCore):
    def __init__(self):
        super.__init__()

    '''
    This command queries the module’s activity status.
    '''    
    def mobileEquipActivityStatus_test(self):
        cmd="AT+CPAS"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute")
        return str(res.body).replace("OK","")
    
    '''
     This command queries the module’s activity status.
    '''
    def mobileEquipmActivityStatus_exec(self):
        cmd="AT+CPAS"
        res=self.execATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute")
        return str(res.body).replace("OK","")
    


    '''
    This command queries an extended error and report the cause of the last failed operation, such as:
        The failure to release a call
        The failure to set up a call (both mobile originated or terminated)
        The failure to modify a call by using supplementary services
        The failure to activate, register, query, deactivate or deregister a supplementary service
        The failure to attach GPRS or the failure to activate a PDP context
        The failure to detach GPRS or the failure to deactivate a PDP context
    '''
    def extendErrorReport_test(self):
        cmd="AT+CEER"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command....")

        return str(res.body).replace("OK","")

    '''
    This command queries an extended error and report the cause of the last failed operation, such as:
        The failure to release a call
        The failure to set up a call (both mobile originated or terminated)
        The failure to modify a call by using supplementary services
        The failure to activate, register, query, deactivate or deregister a supplementary service
        The failure to attach GPRS or the failure to activate a PDP context
        The failure to detach GPRS or the failure to deactivate a PDP context
    '''
    def errorExtendReport_exec(self): 
        cmd="AT+CEER"
        res=self.execATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command .......")

        return str(res.body).replace("OK","")

    '''
    This command controls URC indication.
    '''       
    def URCIndicationConfiguration_test(self):
        cmd="AT+QINDCFG"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ..........")

        return str(res.body).replace("OK","")
    
    '''
    This command controls URC indication.
    '''
    def URCIndicationConfiguration_write(self,urctype,enable,save_to_nvram=0):
        cmd="AT+QINDCFG"
        res=self.wrATCMD(cmd,[urctype,enable,save_to_nvram])
        if(res.status==True):
            dbg("failed to execute command ..........")      


    
    '''
    MBN File Configuration Setting
    '''
    def MBNFileConfigSetting_test(self):
        cmd="AT+QMBNCFG"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ......")

        return str(res.body).replace("OK","")
    
    '''
    MBN File Configuration List
    '''
    def MBNFileConfigSetting_List(self):
        cmd="AT+QMBNCFG"
        res=self.wrATCMD(cmd,"List")
        if(res.status!=True):
            dbg("failed to execute command ....")

        return str(res.body).replace("OK","")
    

    '''
    MBN File Configuration select
    '''
    def MBNFileConfigSetting_Select(self,MBNName):
        cmd="AT+QMBNCFG"
        res=self.wrATCMD(cmd,["Select",MBNName])
        if(res.status!=True):
            dbg("failed to execute command .........")

        return str(res.body).replace("OK","")


    '''
    MBN File Configuration Deactivate
    '''
    def MBNFileConfigSetting_Deactivate(self):
        cmd="AT+QMBNCFG"
        res=self.wrATCMD(cmd,["Deactivate"])
        if(res.status!=True):
            dbg("failed to execute command ........")
        return str(res.body).replace("OK","")


    '''
    MBN File Configuration AutoSel
    ''' 
    def MBNFileConfigSetting_AutoSel(self):
        cmd="AT+QMBNCFG"
        res=self.wrATCMD(cmd,["AutoSel"])
        if(res.status!=True):
            dbg("failed to execute command ......")
        return str(res.body).replace("OK","")

    
    '''
    MBN File Configuration Add
    '''
    def MBNFileConfigSetting_Add(self,fileName):
        cmd="AT+QMBNCFG"
        res=self.wrATCMD(cmd,["Delete",fileName])
        if(res.status!=True):
            dbg("failed to execute command .......")

        return str(res.body).replace("OK","")


    '''
    MBN File Configuration Delete
    '''
    def MBNFileConfigSetting_Delete(self,MBNName):
        cmd="AT+QMBNCFG"
        res=self.wrATCMD(cmd,["Delete",MBNName])
        if(res.status!=True):
            dbg("failed to execute command .......")
        return str(res.status!=True)
    
    '''
    MBN File Configuration List_all
    '''
    def MBNFileConfiguration_ListAll(self):
        cmd="AT+QMBNCFG"
        res=self.wrATCMD(cmd,["List_all"])
        if(res.status!=True):
            dbg("failed to execute command ....... ")

        return str(res.body).replace("OK","")

