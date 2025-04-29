### **Problem 1661: Average Time to Process per machine**

-- Calculate average processing time for each machine
select a1.machine_id, round(avg(a2.timestamp - a1.timestamp), 3) as processing_time
from activity a1
join activity a2
on a1.machine_id = a2.machine_id           -- Match activities from the same machine
and a1.process_id = a2.process_id           -- and same process
and a1.activity_type = 'start'              -- a1 must be a 'start' activity
and a2.activity_type = 'end'                -- a2 must be the corresponding 'end' activity
group by 1;                                 -- Group by machine_id
