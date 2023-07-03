# Write your MySQL query statement below
# select round((100*count(if(t1.first_order=Delivery.customer_pref_delivery_date,t1.first_order,null))/count(*) ),2) as  immediate_percentage
# from
# (Delivery inner join
# (select delivery_id, customer_id, min(order_date) as first_order
# from Delivery
# group by customer_id) t1 using(delivery_id) )

select round((100*count(if(order_date=customer_pref_delivery_date,order_date,null))/count(*) ),2) as  immediate_percentage
from Delivery 
where (customer_id, order_date) in
(select customer_id, min(order_date) as first_order
from Delivery 
group by customer_id)





# # Write your MySQL query statement below
# select round(sum(if(order_date = customer_pref_delivery_date, 1, 0)) / count(*) * 100, 2) as immediate_percentage from Delivery
# where (customer_id, order_date) in
# (
#     Select customer_id, min(order_date) from Delivery group by customer_id
# )