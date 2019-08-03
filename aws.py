from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("MQTTC")
myMQTTClient.configureEndpoint("AWS URL",8883)
myMQTTClient.configureCredentials("PATH TO CA.pem","PATH TO *-private.pem.key","PATH TO *-certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)
myMQTTClient.connect()
myMQTTClient.publish("thing01/info","connected",0)

myMQTTClient.publish("thing01/data","3",0)
