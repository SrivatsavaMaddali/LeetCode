# Write your MySQL query statement below
select name from Employee
where id in (
   select managerId 
   from (
    select managerId, count(id) as cnt
from Employee
    group by managerId ) as a
    where a.cnt>=5
 )
