# iot_anomaly_analytics
Simulates a serverless IoT data processing pipeline using the following AWS services:
- Kinesis (Firehose, Streams & Analytics)
- CloudFormation
- Athena
- Lambda
- SNS
- S3
- IAM

Notably absent from this list is AWS IoT - given that the focus is on data processing, this demo architecture "short circuits" the data flow and goes right from the data producer script directly to a Kinesis Firehose delivery stream. IRL, you would have AWS IoT as your message broker / security guard / life coach :)

The data generator scripts assume a few things:
- You have Python 2.7 installed
- You have boto3 installed
- You have your AWS credentials configured locally and those credentials can put records to your Kinesis Firehose delivery stream 

### Instructions (**very** raw at this point)

#### Anomaly Detection with Kinesis Analytics
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
- Run the generate_single_anomaly python script **once** - confirm you received an email alerting you to an anomaly. You can run this as many times as you like, but make sure to give about a minute or so between executions to make sure that the anomalies don't become the norm. You can play around with the sensitivity / time decay in the Kinesis Analytics SQL console.

#### Analytics using Athena
- All this time, data has been accumulating in your S3 bucket. Time to run some interactive queries against it.
- In the Athena console, go to the Catalog Manager tab.
- Click on 'Add table'.
- Create a new database, naming it whatever you want, also providing a name for the table.
- The location of your dataset will be s3:// + your S3 bucket name with a trailing /
- Use JSON as data format.
- There are 3 columns to create:
  - deviceId - string
  - sensorReading - smallint
  - readingTimestamp - timestamp
- Skip partitioning and create table.
- Query your data! Some examples are in athena-examples.sql
