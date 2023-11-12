'''
@Author : infinity tech ltd http://infinitytech.ltd/
@date   : 23 Sep 2023
@file   : test_gsmCore.py
@brief  : this code will be responsible for handring AT commands 

'''

import sys

new_path = '../../devices/gsm4G'
new_path2 = '../'

sys.path.append(new_path2)
sys.path.append(new_path)


from gsmCore import GsmCore 
from gsmGeneral import GsmGeneral



def debugResponse(resp):
    if (resp.status == True):
        print("command executed ....")
        print(resp.body) 
    else:
        print("failed to execute command..")
        print(resp.body)  





mygsm = GsmCore()


# execute command test
res = mygsm.execATCMD("ATI")
debugResponse(res)


# read command test
res = mygsm.readATCMD("ATI")    
debugResponse(res)


# test command test
res = mygsm.testATCMD("ATI")    
debugResponse(res)


# test command test
res = mygsm.wrATCMD("ATI",[123,"abc","xyz"])    
debugResponse(res)

print("_____________________GSM GENERAL______________________")

myggeneral = GsmGeneral()
myggeneral.displayMTIdentificationInfo()
