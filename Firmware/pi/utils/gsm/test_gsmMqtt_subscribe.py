import sys
import time

new_path = '../../devices/gsm4G'

sys.path.append(new_path)
from Quectel import Quectel


myMQTT_Subscriber=Quectel()


myMQTT_Subscriber.initMQTT()
myMQTT_Subscriber.mqttSubscribe("ss")

while True:
    pass

