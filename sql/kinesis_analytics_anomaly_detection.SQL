--Creates a temporary stream.
CREATE OR REPLACE STREAM "TEMP_STREAM" (
	        "sensorReading"        SMALLINT,
	        "deviceId"         varchar(4),
	        "ANOMALY_SCORE"    DOUBLE);

--Creates another stream for application output.
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
	        "sensorReading"        SMALLINT,
	        "deviceId"         varchar(4),
	        "ANOMALY_SCORE"    DOUBLE);

-- Compute an anomaly score for each record in the input stream
-- using Random Cut Forest
CREATE OR REPLACE PUMP "STREAM_PUMP" AS
   INSERT INTO "TEMP_STREAM"
      SELECT STREAM "sensorReading", "deviceId", ANOMALY_SCORE
      FROM TABLE(RANDOM_CUT_FOREST(
            -- See http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/random-cut-forest.html
            -- for an explaination of the function parameters below.
            -- The important number is 120 - that is our timeDecay.
              CURSOR(SELECT STREAM * FROM "SOURCE_SQL_STREAM_001"), 100, 256, 120, 1));

-- Sort records by descending anomaly score, insert into output stream
CREATE OR REPLACE PUMP "OUTPUT_PUMP" AS
   INSERT INTO "DESTINATION_SQL_STREAM"
      SELECT STREAM * FROM "TEMP_STREAM"
      WHERE ANOMALY_SCORE > 4 -- To keep things simple, define an important anomaly as an item with an ANOMALY_SCORE greater than 4
      ORDER BY FLOOR("TEMP_STREAM".ROWTIME TO SECOND), ANOMALY_SCORE DESC;
