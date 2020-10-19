import json
import boto3
from model.aws.ec2 import Marshaller
from model.aws.ec2 import AWSEvent
from model.aws.ec2 import EC2InstanceStateChangeNotification

client = boto3.client('iot-data')

def lambda_handler(event, context):
    response = client.publish(
        topic='alarm',
        qos=0
    )

    #Deserialize event into strongly typed object
    awsEvent:AWSEvent = Marshaller.unmarshall(event, AWSEvent)
    ec2StateChangeNotification:EC2InstanceStateChangeNotification = awsEvent.detail

    #Execute business logic
    print("Instance " + ec2StateChangeNotification.instance_id + " transitioned to " + ec2StateChangeNotification.state)

    #Make updates to event payload
    awsEvent.detail_type = "HelloWorldFunction updated event of " + awsEvent.detail_type;

    #Return event for further processing
    return Marshaller.marshall(awsEvent)
