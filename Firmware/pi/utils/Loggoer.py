'''
@Author : infinity tech ltd http://infinitytech.ltd/
@date   : 23 Sep 2023
@file   : Logger.py
@brief  : this code will be responsible for logging errors occure in our organizatiion

'''



import os

logfilePath = '/media/nader/rootfs/home/pi/log/log.txt'
logdirpath  = '/media/nader/rootfs/home/pi/log/'


class Logger():
    def __init__(self,moduleName):
        self.moduleName=moduleName

    def Log(self,msg):
        try:
            with open(logfilePath, 'a') as file:
                content=self.moduleName+msg+'\n'+"************************************"+'\n'
                file.write(content)
        except :
            new_directory = logdirpath
            if not os.path.exists(new_directory):
                os.mkdir(new_directory)
                # print(f"Directory '{new_directory}' created successfully.")
                with open(logfilePath, 'a') as file:
                    content=self.moduleName+msg+'\n'+"************************************"+'\n'
                    file.write(content)
            else:
                print(f"Directory '{new_directory}' already exists.")


                    
            
