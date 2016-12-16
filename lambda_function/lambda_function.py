from __future__ import print_function

import base64
import json
import boto3
import os

# connect to SNS
client = boto3.client('sns')

print('Loading function')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        print("Decoded payload: " + payload)
        print("SNS topic ARN: " + os.environ['SnsTopicArn'])
        print("Sending anomaly information to SNS topic")
        response = client.publish(
            TopicArn=os.environ['SnsTopicArn'],
            Message=payload,
            Subject='Anomaly Detected!',
            MessageStructure='string',
        )

    return 'Successfully processed {} records.'.format(len(event['Records']))
