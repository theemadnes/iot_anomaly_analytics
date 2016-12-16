import random
import boto3
import datetime
import time
import json
import settings

client = boto3.client('firehose')

payload = {
    'deviceId' : random.choice(settings.device_ids), # select a random device
    'sensorReading' : random.choice([random.randint(400,500),random.randint(-500,-400)]),
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
