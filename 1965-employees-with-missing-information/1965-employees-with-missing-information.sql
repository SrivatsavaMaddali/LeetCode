# Write your MySQL query statement below
select * from 
(
(select e.employee_id as employee_id
from Employees e, Salaries s
where e.employee_id not in (select s.employee_id from Salaries s))
union
(select s.employee_id as employee_id
from Employees e, Salaries s
where s.employee_id not in (select e.employee_id from Employees e))
) t
order by employee_id