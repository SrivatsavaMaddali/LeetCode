# Write your MySQL query statement below
select *
from
(
(select new_id as id,student
from(
select *,
case
when mod(id,2)=0 then id-1
when mod(id,2)=1 then id+1
end as new_id
from Seat
where id not in(select max(id) from Seat)) t
order by new_id )
union
(select case
 when mod(id,2)=0 then id-1
 when mod(id,2)=1 then id
 end as id
 ,student
 from Seat
    where id in (select max(id) from Seat))
    ) c
    order by id