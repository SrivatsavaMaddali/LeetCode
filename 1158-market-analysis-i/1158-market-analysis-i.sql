# Write your MySQL query statement below

select u.user_id as buyer_id,u.join_date as join_date,if(t.orders_in_2019 is null,0,t.orders_in_2019) as orders_in_2019 
from Users u left join (
select o.buyer_id, count(*) as orders_in_2019
from Orders o 
where year(o.order_date)=2019
group by o.buyer_id) t
on u.user_id=t.buyer_id