# Write your MySQL query statement below
select name, bonus
from Employee left outer join Bonus using(empId)
where bonus<1000 or bonus is null