import boto3

client = boto3.client("sns","us-east-1")

phone =input("Enter Phone No:")
EndMsg = input("Enter Msg")

Msg = client.publish(PhoneNumber= phone,Message = EndMsg)

print(Msg)