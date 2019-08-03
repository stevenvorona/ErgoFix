import RPi.GPIO as GPIO
import time
import sys
import serial

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("MQTTC CLIENT")
myMQTTClient.configureEndpoint("ENDPOINT URL",8883)
myMQTTClient.configureCredentials("PATH TO ca.pem","PATH TO ...private.pem.key","PATH TO ...certificate.pem.crt")
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
        butt = float(vals[0])
        back = float(vals[1])
        myMQTTClient.publish("AWSButt/data",butt,0)
        myMQTTClient.publish("AWSBack/data",back,0)
	time.sleep(0.1)
        print val
	sys.stdout.flush()
