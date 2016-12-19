import random
import boto3
import datetime
import time
#import json
import settings

client = boto3.client('firehose')

# modifying original script that used JSON as payload to send data in CSV format
# removing timestamp from script - will depend on timestamp applied by Kinesis

# run forever
while True:

    # simulate each device sending its telemetry data
    for device_id in settings.device_ids:
        # commenting out JSON
        '''payload = {
            'deviceId' : device_id,
            'sensorReading' : random.randint(-5,5),
            'readingTimestamp' : datetime.datetime.utcnow().isoformat()
        }'''
        payload = device_id + ',' + '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ',' + str(random.randint(-5,5)) + '\n'
        # print("Sending payload to Kinesis: " + json.dumps(payload))
        print("Sending payload to Kinesis: " + payload)
        print(client.put_record(
            DeliveryStreamName=settings.delivery_stream_id,
            Record={
                # 'Data': json.dumps(payload)
                'Data': payload
            }
            )
        )

    time.sleep(1)
