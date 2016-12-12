import random
import boto3
import datetime
import time
import base64
import json

# set up device list & kinesis info
devices = ["aaaa", "bbbb", "cccc", "dddd", "eeee"]
delivery_stream_id = "hhhhgggg-DataKinesisFirehose-1RKTJYBTNYXZO"

# random.randint(-5,5)

client = boto3.client('firehose')
'''
response = client.put_record_batch(
    DeliveryStreamName=delivery_stream_id,
    Records=[
        {
            'Data': b'bytes'
        },
    ]
)
'''

# simulate each device sending its telemetry data
for device in devices:
    payload = {
        'deviceId' : device,
        'sensorReading' : random.randint(-5,5),
        'readingTimestamp' : datetime.datetime.utcnow().isoformat()
    }
    print(client.put_record(
        DeliveryStreamName=delivery_stream_id,
        Record={
            'Data': json.dumps(payload)
        }
        )
    )
