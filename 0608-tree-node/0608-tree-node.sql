# Write your MySQL query statement below
select t2.id as id, (case
when (select t1.p_id from Tree t1 where t1.id=t2.id) is null then "Root" 
when (select count(*) from Tree t3 where t3.p_id = t2.id) = 0 THEN "Leaf"
else "Inner"
end) as type
from Tree t2