-- SELECT * FROM anomaly.a1 WHERE sensorreading ;
SELECT count(*) as records FROM anomaly.a1 GROUP BY deviceid;
