# iot_anomaly_analytics
Process data ingestion to perform both anomaly detection via Kinesis Analytics and store data for analytics with Athena

### Instructions (**very** raw at this point)

- Deploy CloudFormation template - note the outputs
  - Provide an email address that you own, as this is where you will receive anomaly detection alerts. You'll be sent a subscription confirmation email - make sure to confirm.
- update settings.py to point to your Firehose delivery stream
- start the data generator script (not the generate single anomaly script)
- after a minute or so, you should see data populating in your S3 bucket, organized by time
- in the Kinesis Analytics console (Kinesis -> Go to Analytics), create a new application
  - Provide some name that is meaningful to you
  - Define your source as the Firehouse delivery stream, using the IAM role created for Kinesis Analytics by CloudFormation
  - in the SQL editor, cut & paste the SQL from kinesis_analytics_anomaly_detection.SQL - this code uses the random cut forest function to calculate an anomaly score for each data record
  - Set the Kinesis stream as the destination
- In the Lambda console, set the trigger for your lambda function to the Kinesis anomaly stream, with a batch size of 1.
