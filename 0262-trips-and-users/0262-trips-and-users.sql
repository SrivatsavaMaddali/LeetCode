WITH nonbannedtrips AS (
    SELECT *
    FROM Trips
    WHERE client_id NOT IN (
        SELECT users_id
        FROM Users
        WHERE banned = 'Yes'
    )
    AND driver_id NOT IN (
        SELECT users_id
        FROM Users
        WHERE banned = 'Yes'
    )
    and request_at between "2013-10-01" and "2013-10-03"
)

SELECT request_at as Day,
       ROUND((COUNT(IF(n.status = 'cancelled_by_driver' OR n.status = 'cancelled_by_client', 1, NULL)) / COUNT(*)), 2) as 'Cancellation Rate'
FROM nonbannedtrips n
GROUP BY request_at
