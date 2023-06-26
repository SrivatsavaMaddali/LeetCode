# Write your MySQL query statement below
select distinct l.num as ConsecutiveNums
from Logs l, Logs m, Logs n
where l.num=m.num and l.num=n.num and l.id=m.id-1 and m.id=n.id-1