# Write your MySQL query statement below
select a.visited_on as visited_on, sum(c.amount) as amount, round(avg(c.amount),2) as average_amount
from (select visited_on, sum(amount) as amount from Customer group by visited_on ) c,
(select visited_on, sum(amount) as amount from Customer group by visited_on ) a
where datediff(a.visited_on,c.visited_on) between 0 and 6
group by a.visited_on
having count(a.visited_on)=7
order by visited_on