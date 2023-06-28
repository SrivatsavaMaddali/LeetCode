# # Write your MySQL query statement below
# select q.query_name, round(avg(rating/position),2) as quality, round(100*t.cnt/count(*),2) as poor_query_percentage
# from Queries q, (select query_name,count(*) as cnt from Queries where rating<3 group by query_name) t
# where q.query_name=t.query_name
# group by query_name

select query_name, 
ROUND(AVG(rating / position), 2) AS quality,
round(SUM(rating<3)/count(query_name)*100,2) as poor_query_percentage 
from queries
group by query_name;
