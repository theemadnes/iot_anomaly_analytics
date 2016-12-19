# iot_anomaly_analytics
Process data ingestion to perform both anomaly detection via Kinesis Analytics and store data for analytics with Athena

### Instructions (incomplete)

- Deploy CloudFormation template - note the outputs
- update settings.py to point to your Firehose delivery stream
- start the data generator script (not the generate single anomaly script)
- after a minute or so, you should see data populating in your S3 bucket, organized by time
