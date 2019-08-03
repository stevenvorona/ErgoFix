import RPi.GPIO as GPIO
import time
import sys
import serial
#from hx711 import HX711

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("123afhlss456")
myMQTTClient.configureEndpoint("a3c8vkme4nieo5.iot.us-east-2.amazonaws.com",8883)
myMQTTClient.configureCredentials("/home/pi/cert/CA.pem","/home/pi/cert/a398f6d552-private.pem.key","/home/pi/cert/a398f6d552-certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)
myMQTTClient.connect()
myMQTTClient.publish("thing01/info","connected",0)

myMQTTClient.publish("thing01/data","3",0)


ser = serial.Serial('/dev/ttyACM0', 38400)

def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

butt = 0
back = 0
while True:
    for i in range(0, 1):
        val = ser.readline()[:len(ser.readline())-2]
        vals = val.split(',')
        butt = str(vals[0])
        back = str(vals[1])
        myMQTTClient.publish("AWSData/butt",butt,0)
        myMQTTClient.publish("AWSData/back",back,0)
	time.sleep(0.1)
        print val
	sys.stdout.flush()
