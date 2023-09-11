# Write your MySQL query statement below
select distinct t1.*
from
(
(select *
from Stadium
where people>=100) t1
cross join
(select *
from Stadium
where people>=100) t2
cross join
(select *
from Stadium
where people>=100) t3
) 
where  ((t1.id-t2.id=1 and t1.id-t3.id=2 and t2.id-t3.id=1)
    or
    (t2.id-t1.id=1 and t2.id-t3.id=2 and t1.id-t3.id=1)
    or
    (t3.id-t2.id=1 and t2.id-t1.id=1 and t3.id-t1.id=2) )
order by t1.id
