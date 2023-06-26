# Write your MySQL query statement below
(
    select u.name as results 
from users u left join Movierating m on u.user_id=m.user_id 
group by u.name 
order by count(m.movie_id) desc, u.name limit 1
)
union all
(
  select results from (
select mo.title as results,m.created_at 
from MovieRating m left join Movies mo on mo.movie_id=m.movie_id 
where year(m.created_at)=2020 and month(m.created_at)=2
group by mo.title 
order by avg(m.rating) desc, mo.title limit 1) a
)