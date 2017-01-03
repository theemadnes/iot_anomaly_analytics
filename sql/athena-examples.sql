-- in these examples my database is named 'anomaly' and my table is named 'a2'

-- find entries outside of the expected -5 to 5 range
SELECT * FROM anomaly.a2 WHERE sensorreading < -5 or sensorreading > 5;

-- count # of records per deviceId
SELECT COUNT(*) AS records FROM anomaly.a2 GROUP BY deviceid;

-- find max reading per deviceId
SELECT deviceid, MAX(sensorreading) AS maxreading FROM anomaly.a2 GROUP BY deviceid;

-- find min reading per deviceId
SELECT deviceid, MIN(sensorreading) AS minreading FROM anomaly.a2 GROUP BY deviceid;
