# Write your MySQL query statement below
select a as id,cnt as num from 
(
select a,count(a) as cnt
from(
(select accepter_id as a from RequestAccepted)
union all
(select requester_id as a from RequestAccepted)
    ) t
group by a) t1

where cnt =(SELECT MAX(cnt) FROM (select a,count(a) as cnt
from(
(select accepter_id as a from RequestAccepted)
union all
(select requester_id as a from RequestAccepted)
    ) t
group by a)t3) 