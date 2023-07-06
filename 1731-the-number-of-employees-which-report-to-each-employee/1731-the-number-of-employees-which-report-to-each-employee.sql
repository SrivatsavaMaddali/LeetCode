# Write your MySQL query statement below
select a.employee_id,a.name,t.reports_count,t.average_age
from Employees a join
(select reports_to as eid,count(employee_id) as reports_count, round(avg(age)) as average_age 
from Employees
group by reports_to
having count(employee_id)>=1) t on a.employee_id=t.eid
order by a.employee_id