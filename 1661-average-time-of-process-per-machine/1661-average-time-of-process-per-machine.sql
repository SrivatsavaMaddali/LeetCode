# Write your MySQL query statement below
select machine_id,round(sum(tim)/count(*),3) as processing_time
from
(select a1.machine_id, a1.process_id, (a2.timestamp-a1.timestamp) as tim
from Activity a1, Activity a2
where a1.machine_id=a2.machine_id and a1.process_id=a2.process_id and a1.activity_type='start' and a2.activity_type='end') com
group by machine_id