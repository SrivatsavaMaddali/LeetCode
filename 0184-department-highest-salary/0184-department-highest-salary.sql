# Write your MySQL query statement below
select t2.dname as Department, e3.name as Employee, t2.high as Salary
from 
(select d.id as did,d.name as dname,t1.high as high from (select departmentId,max(salary) as high
from Employee e1
group by departmentId) t1 join Department d on t1.departmentId=d.id) t2,Employee e3
where e3.departmentId=t2.did and e3.salary=t2.high