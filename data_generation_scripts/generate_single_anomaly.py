import random
import boto3
import datetime
import time
#import json
import settings

client = boto3.client('firehose')

# modifying original script that used JSON as payload to send data in CSV format
# removing timestamp from script - will depend on timestamp applied by Kinesis

# commenting out JSON
'''payload = {
    'deviceId' : random.choice(settings.device_ids), # select a random device
    'sensorReading' : random.choice([random.randint(400,500),random.randint(-500,-400)]),
    'readingTimestamp' : datetime.datetime.utcnow().isoformat()
}'''
payload = random.choice(settings.device_ids) + ',' + '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ',' + str(random.randint(-5,5)) + '\n'

# print("Sending payload to Kinesis: " + json.dumps(payload))
print("Sending payload to Kinesis: " + payload)
print(client.put_record(
    DeliveryStreamName=settings.delivery_stream_id,
    Record={
        'Data': payload
    }
    )
)
