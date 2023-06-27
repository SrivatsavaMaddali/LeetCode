# Write your MySQL query statement below
SELECT a.id
FROM Weather a, Weather b
WHERE a.temperature > b.temperature 
AND a.recordDate=DATE_ADD(b.recordDate, INTERVAL 1 DAY)