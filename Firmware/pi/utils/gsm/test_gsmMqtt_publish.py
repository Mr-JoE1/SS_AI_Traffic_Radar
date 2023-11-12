import sys
import time

new_path = '../../devices/gsm4G'

sys.path.append(new_path)
from Quectel import Quectel


myMQTT_Publisher=Quectel()


myMQTT_Publisher.initMQTT()

while True:
    myMQTT_Publisher.mqttpublish("ss","hello world using Quectel LTE MQTT")
    time.sleep(1.5)

