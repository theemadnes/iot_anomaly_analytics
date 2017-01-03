-- a small collection of really simple queries to run against your data for this demo
-- in these examples my database is named 'anomaly' and my table is named 'a2'

-- find entries outside of the expected -5 to 5 range
SELECT * FROM anomaly.a2 WHERE sensorreading < -5 or sensorreading > 5;

-- count # of records by deviceId
SELECT COUNT(*) AS records FROM anomaly.a2 GROUP BY deviceid;

-- find max reading by deviceId
SELECT deviceid, MAX(sensorreading) AS maxreading FROM anomaly.a2 GROUP BY deviceid;

-- find min reading by deviceId
SELECT deviceid, MIN(sensorreading) AS minreading FROM anomaly.a2 GROUP BY deviceid;

-- find average reading by deviceId
SELECT deviceid, AVG(sensorreading) AS avgreading FROM anomaly.a2 GROUP BY deviceid;
