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
        print(str(current_time_ms)+"  GsmNetwork:"+msg+" \n")
    else:
        print(status, str(current_time_ms)+"  GsmNetwork:"+msg+"\n")



class GsmNetwork(GsmCore):
    def __init__(self):
        super.__init__()


    '''
    This Test Command returns a set of five parameters, each representing an operator presenting in the
    network. Any of the formats may be unavailable and should then be an empty field. The list of operators
    shall be in the order of: home network, networks referenced in (U)SIM and other networks.
    '''
    def opereatorSelector_test(self):
        cmd="AT+COPS"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ......")

        return res.body.replace("OK","")

    '''
    This Read Command returns the current mode and the currently selected operator. If no operator is
    selected, <format>, <oper> and <Act> are omitted.
    '''   
    def opereatorSelector_read(self):
        cmd="AT+COPS"
        res=self.readATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ........")
        return res.body.replace("OK","")
    
    '''
    This Write Command forces an attempt to select and register the GSM/UMTS network operator. If the
    selected operator is not available, no other operator shall be selected (except <mode>=4). The format of
    selected operator name shall apply to further Read Command (AT+COPS?).
    '''
    def opereatorSelector_write(self,mode,format,oper,act):
        cmd="AT+COPS"
        res=self.wrATCMD(cmd,[mode,format,oper,act])
        if(res.status!=True):
            dbg("failed to execute command .......")
        return res.body.replace("OK","")

    

    '''
    This Read Command returns the status of result code presentation and an integer <stat> which shows
    whether the network has currently indicated the registration of the ME. Location information elements
    <LAC> and <ci> are returned only when <n>=2 and ME is registered on the network.
    '''
    def networkRegestrationStatus_read(self):
        cmd="AT+CREG"
        res=self.readATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ....")
        return res.body
    
    '''
    This Write Command controls the presentation of an unsolicited result code +CREG: <stat> when <n>=1
    and there is a change in the ME network registration status.
    '''
    def networkRegestrationStatus_write(self,n):
        cmd="AT+CREG"
        res=self.wrATCMD(cmd,[n])
        if(res.status!=True):
            dbg("failed to execute command ......")
        return res.body.replace("OK","")
    
    '''
    This command indicates the received signal strength <rssi> and the channel bit error rate <ber>.
    This Test Command returns values supported by MT.
    '''
    def signalQualityReport_test(self):
        cmd="AT+CSQ"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ......")
        return res.body.replace("OK","")

    '''
    This Execution Command returns received signal strength indication <rssi> and channel bit error rate
    <ber> from MT.
    '''
    def signalQualityReport_exec(self):
        cmd="AT+CSQ"
        res=self.execATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ........")
        return res.body.replace("OK","")
    


    '''
    returns the list of the supported operator names from MT. Each operator code
    <numericn> that has an alphanumeric equivalent <alphan> in the MT memory is returned.
    '''
    def readOpereatorNames(self):
        cmd="AT+COPN"
        res=self.execATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command .......")

        return res.body.replace("OK","")
    
    '''
    This command enables/disables automatic time zone update via NITZ.
    '''
    def getAutoTimeZoneUpdateStatus(self):
        cmd="AT+CTZU"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command .....")

        return res.body.replace("OK","")


    '''
    This command enables/disables automatic time zone update via NITZ.
    '''
    def setAutoTimeZoneUpdate(self,op):
        cmd="AT+CTZU"
        res=self.wrATCMD(cmd,[op])
        if(res.status!= True):
            dbg("failed to execute command ......")

        return res.body.replace("OK","")
    

    '''
    This command queries network information such as the selected access technology, operator and band.
    '''
    def queryNetworkInfo(self):
        cmd="AT+QNWINFO"
        res=self.execATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute the command .......")
        data=res.body.replace("+QNWINFO:","")
        data=data.replace("OK","")
        params=data.split(",")
        Act=params[0]
        oper=params[1]
        band=params[2]
        channel=params[3]
        return Act,oper,band,channel

    '''
    Display the Name of Registered Network
    '''  
    def displayRegisteredNetworkName(self):
        cmd="AT+QSPN"
        res=self.execATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command .....")

        data=res.body.replace("OK","")
        data=data.replace("+QSPN:","")
        params=data.split(",")
        FNN=params[0]
        SNN=params[1]
        SPN=params[2]
        alphabet=params[3]
        RPLMN=params[4]
        return FNN,SNN,SPN,alphabet,RPLMN
    
    
    '''
    Query Network Information of RATs
    '''
    def getNetworkInfoRATs(self):
        cmd="AT+QNETINFO"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ......")
        data=res.body.replace("OK","")
        data=data.replace("+QNETINFO:")
        params=data.split(",")
        rat=params[0]
        bit_msk=params[1]
        return rat,bit_msk
    
    '''
    Query Network Information of RATs
    '''
    def getNetworlInfoRATs(self,rat,bit_msk):
        cmd="AT+QNETINFO"
        res=self.wrATCMD(cmd,[rat,bit_msk])
        if(res.status!=True):
            dbg("failed to execute command......")
        data=res.body.replace("OK","")
        data=data.replace("+QNETINFO:","")
        params=data.split(",")
        mode=params[0]
        rslt_cnt=params[0]
        functions = {}
        for i in range(len(params)):
            if(params[i]==mode or params[i]==rslt_cnt):
                pass
            functions[params[i]]=params[i+1]
            i=i+2
        return mode,rslt_cnt,functions
    
    '''
    Network Locking Configuration
    '''
    def getNetworkLockingConfig(self):
        cmd="AT+QNWLOCK"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ......")
        data=res.body.replace("OK","")
        data=data.replace("+QNWLOCK:","")
        data=data.replace("]]]","")
        data=data.replace("[,","")
        params=data.split(",")
        commonLTE=params[0]
        action=params[1]
        EARFCN=params[2]
        PCI=params[3]
        status=params[4]
        return commonLTE,action,EARFCN,PCI,status

    '''
    Configure Bands to be Scanned in 2G/3G/4G
    '''   
    def configBandToBeScanned(self,RAT,GW_band,LTE_band,TDS_band):
        cmd="AT+QOPSCFG"
        res=self.wrATCMD(cmd,[RAT,GW_band,LTE_band,TDS_band])
        if(res.status!=True):
            dbg("failed to execute command ......... ")
        data=res.body.replace("OK","")
        data=data.replace("+QOPSCFG:","")
        params=data.split(",")
        scancontrol=params[0]
        rat=params[1]
        _GW_band=params[2]
        _LTE_band=params[3]
        _TDS_band=params[4]
        return scancontrol,rat,_GW_band,_LTE_band,_TDS_band

    '''
    Enable/Disable to Display RSSI in LTE
    '''
    def setDisplayRSSI_LTE(self,en):
        cmd="AT+QOPSCFG"
        res=self.wrATCMD(cmd,[en])
        if(res.status!=True):
            dbg("failed to execute command")

    
    '''
    This command triggers band scan. The Execution Command lists the available network information of
    operators for all neighbor cell.
    '''
    def scanBand(self):
        cmd="AT+QOPS"
        res=self.execATCMD(cmd)
        if(res.status!=True):
           dbg("failed to execute command ")
        data=res.body.replace("OK")
        data=data.replace("+QOPS:","")
        params=data.split(",")
        if(len(params)>12):
            oper_in_string=params[0]
            oper_in_short_string=params[1]
            oper_in_number=params[2]
            index=params[3]
            RAT=params[4]
            freq=params[5]
            lac=params[6]
            ci=params[7]
            bsic=params[8]
            rxlev=params[9]
            c1=params[10]
            cba=params[11]
            is_gprssupport=params[12]
            return oper_in_string,oper_in_short_string,oper_in_number,index,RAT,freq,lac,ci,bsic,rxlev,c1,cba,is_gprssupport                
        else :
            oper_in_string=params[0]
            oper_in_short_string=params[1]
            oper_in_number=params[2]
            index=params[3]
            RAT=params[4]
            freq=params[5]
            psc=params[6]
            lac=params[7]
            ci=params[8]
            rscp=params[9]
            ecno=params[10]
            cba=params[11]
            return oper_in_string,oper_in_short_string,oper_in_number,index,RAT,freq,psc,lac,ci,rscp,ecno,cba
        

    '''
    This command configures FPLMN (Forbidden Public Land Mobile Network), including adding a PLMN to
    FPLMN, removing a PLMN from FPLMN list
    '''
    def getFPLMNConfigs(self):
        cmd="AT+QFPLMNCFG"
        res=self.testATCMD(cmd)
        if(res.body!=True):
            dbg("failed to execute command .....")
        data=res.body.replace('+QFPLMNCFG: "List"+QFPLMNCFG: "Add"',"")
        data=data.replace('+QFPLMNCFG: "Delete"',"")
        params=data.split(",")
        PLMN=params[0]
        return PLMN
    
    '''
    set configures FPLMN (Forbidden Public Land Mobile Network), including adding a PLMN to
    FPLMN, removing a PLMN from FPLMN list.
    '''
    def setPLMNConfigs(self,cmdd,PLMN):
        cmd="AT+QFPLMNCFG"
        res=self.wrATCMD(cmd,[cmdd,PLMN])
        if(res.status!=True):
            dbg("failed to execute command .......")

        return res.body.replace("OK","")
    
    '''
    Command of Control Instructions
    '''
    def getControlInstruction(self):
        cmd="AT+CIND"
        res=self.testATCMD(cmd)
        if(res.status!=True):
            dbg("failed to execute command ....... ")
        return res.body.replace("OK","")
    
    