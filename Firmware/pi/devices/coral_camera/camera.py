'''
@Author : infinity tech ltd http://infinitytech.ltd/
@date   : 24 Sep 2023
@file   : camera.py
@brief  : this code will be responsible for controlling coral camera


dependencies : 
    snapshot tool

workAround :
    if we couldn't download this tool from coral debian server
    we can run command "ls /dev | grep vid" , this will be the
    frame buffer of the camera we can easialy copy its content and save 
    it in a file format jpg like this " echo /dev/videoX > file.jpg "
'''


import json
import sys
import time
import threading
from datetime import datetime
from videoGenerator import create_video_from_images

new_path = '../../utils/system/'

from myCmd import Exec

sys.path.append(new_path)

class CoralCamera:
    '''
    focus mode:
        0       Turn off autofocus
        1       one-shot autofocus mode
        2       continuous autofocus mode.
    '''
    def __init__(self):
        with open('/etc/SS/camera/camera.json', 'r') as file:    
            self.content = json.load(file)  
        self.snapshot="--oneshot"
        self.imgFormat="--format"+str(self.content["format"])
        self.imagePrefix="--prefix"+str(self.content["prefix"])
        self.workDir=str(self.content["prefix"])
        if(self.content["focus_mode"]==1):
            cmd="echo "+str(self.content["focus_mode"])+" > /sys/module/ov5645_camera_mipi_v2/parameters/ov5645_af"
            res = Exec(cmd)
            try:
                if(res.returncode!=0):
                    print("failed to initialize camera")
                    self.Record=False
                    thread1 = threading.Thread(target=self.thread)
                    thread1.start()
                    thread1.join()
            except:
                print("camera initialized successfuly........")
            

    
    '''
    this function will take picture
    '''
    def takePic(self):
        cmd="cd "+self.workDir+" && snapshot --oneshot "+self.imgFormat+" "+self.imagePrefix
        res = Exec(cmd)
        try:
            if(res.returncode!=0):
                print("failed to take picture")
        except:
                pass
    

    '''
    this function will help to start video recording
    '''
    def thread(self,fps=30):
        while True:
            if(self.Record==True):
                self.takePic()
                time.sleep(1/fps)


    
    '''
    this function will start video recording
    '''
    def startRecord(self):
       self.startRecord=True


    '''
    this function will stop and save video file
    ''' 
    def stopRecord(self):
        filename = datetime.now().strftime("VID_%Y/%m/%d_%H:%M:%S")
        self.Record=False
        create_video_from_images(self.workDir,filename,30)
        cmd="sudo rm -rf "+self.imagePrefix+"*"
        res=Exec(cmd)
        if(res.returnCode!=0):
            print("failed to delete images....") 


