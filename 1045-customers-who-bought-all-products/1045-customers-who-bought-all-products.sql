# Write your MySQL query statement below
select customer_id 
from (
select customer_id, count(distinct product_key) as cnt
from Customer
group by customer_id) t1
where cnt=(select count(product_key) as cnnt 
          from Product) 