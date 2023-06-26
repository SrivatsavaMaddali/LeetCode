# Write your MySQL query statement below

select u.score,(select count(distinct s.score) from Scores s where s.score>=u.score) as 'rank'
from Scores u
order by u.score desc