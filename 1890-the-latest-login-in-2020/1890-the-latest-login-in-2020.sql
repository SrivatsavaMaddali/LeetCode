# Write your MySQL query statement below
with S as (
select user_id,time_stamp,rank() over(partition by user_id order by time_stamp desc) as r
from Logins
where year(time_stamp)='2020')
select user_id, time_stamp as last_stamp
from S
where r=1