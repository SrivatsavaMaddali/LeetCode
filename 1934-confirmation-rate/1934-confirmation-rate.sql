# Write your MySQL query statement below
SELECT Signups.user_id, ifnull(ROUND(t2.con / t1.tot, 2),0)AS confirmation_rate
FROM Signups
LEFT JOIN (
    SELECT user_id, COUNT(*) AS tot
    FROM Confirmations
    GROUP BY user_id
) t1 ON Signups.user_id = t1.user_id
LEFT JOIN (
    SELECT user_id, COUNT(*) AS con
    FROM Confirmations
    WHERE action = 'confirmed'
    GROUP BY user_id
) t2 ON Signups.user_id = t2.user_id;

