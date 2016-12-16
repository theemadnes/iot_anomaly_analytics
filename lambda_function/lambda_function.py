from __future__ import print_function

import base64
import json
import boto3
import os

print('Loading function')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        print("Decoded payload: " + payload)
        print("SNS topic name: " + os.environ['SnsTopicId'])
    return 'Successfully processed {} records.'.format(len(event['Records']))
