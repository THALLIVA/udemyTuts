import boto3
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()

def SendMsg():
    client = boto3.client("sns", "us-east-1")
    phone = "+919702007220"
    phone1 = "+919870533756"


    EndMsg = "High Temp         Send Using AWS SNS"
    Msg = client.publish(PhoneNumber=phone, Message=EndMsg)
    Msg1 = client.publish(PhoneNumber=phone1, Message=EndMsg)

    print(Msg)


def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if(int(msg.payload) > 30):
        SendMsg()



mqttc.on_message = on_message
mqttc.connect("192.168.0.101", 1883, 60)
mqttc.subscribe("test", 0)
mqttc.loop_forever()




