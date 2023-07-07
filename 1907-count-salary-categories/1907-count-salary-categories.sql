# Write your MySQL query statement below
select category,max(accounts_count) as accounts_count 
from(
(select Pay_Grade as category, count(*) as accounts_count
from 
(select *,
case
when income<20000 then 'Low Salary'
when income>=20000 and income<=50000 then 'Average Salary'
when income>50000 then 'High Salary'
end as Pay_Grade
from Accounts) t
group by Pay_Grade)
union
(select 'Low Salary' as category, 0 as accounts_count
union
select 'Average Salary' as category, 0 as accounts_count
union
select 'High Salary' as category, 0 as accounts_count)
) x
group by category