-- a small collection of really simple queries to run against your data for this demo
-- in these examples my database is named 'analyticsdemo' and my table is named 'devicedata'

-- find entries outside of the expected -5 to 5 range
SELECT * FROM analyticsdemo.devicedata WHERE sensorreading < -5 or sensorreading > 5;

-- count # of records by deviceId
SELECT COUNT(*) AS records FROM analyticsdemo.devicedata GROUP BY deviceid;

-- find max reading by deviceId
SELECT deviceid, MAX(sensorreading) AS maxreading FROM analyticsdemo.devicedata GROUP BY deviceid;

-- find min reading by deviceId
SELECT deviceid, MIN(sensorreading) AS minreading FROM analyticsdemo.devicedata GROUP BY deviceid;

-- find average reading by deviceId
SELECT deviceid, AVG(sensorreading) AS avgreading FROM analyticsdemo.devicedata GROUP BY deviceid;
