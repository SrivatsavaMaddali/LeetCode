# Write your MySQL query statement below
select s.name
from SalesPerson s
where s.sales_id not in (
select o.sales_id from Orders o where o.com_id in 
(select c.com_id
from Company c
where c.name='RED'))


# SELECT s.name
# FROM SalesPerson s
# WHERE s.sales_id NOT IN (
#   SELECT o.sales_id
#   FROM Orders o
#   JOIN Company c
#   ON c.com_id=o.com_id
#   WHERE c.name='RED'
# )