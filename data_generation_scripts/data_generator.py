import random
import boto3
import datetime
import time
import json
import settings

client = boto3.client('firehose')

# run forever
while True:

    # simulate each device sending its telemetry data
    for device in settings.devices:
        payload = {
            'deviceId' : device,
            'sensorReading' : random.randint(-5,5),
            'readingTimestamp' : datetime.datetime.utcnow().isoformat()
        }
        print("Sending payload to Kinesis: " + json.dumps(payload))
        print(client.put_record(
            DeliveryStreamName=settings.delivery_stream_id,
            Record={
                'Data': json.dumps(payload)
            }
            )
        )

    time.sleep(1)
