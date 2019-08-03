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
