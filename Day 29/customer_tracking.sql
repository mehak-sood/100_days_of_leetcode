-- Number the customer's tracking states by time order
with cte as (
    select *, row_number() over(partition by cust_id order by timestamp asc) as rn
    from cust_tracking
)

-- Join each 'entry' state with the immediately next 'exit' state for the same customer
select 
    t1.cust_id, 
    -- Calculate time spent in seconds, divide by 3600 to convert to hours
    sum(timestampdiff(second, t1.timestamp, t2.timestamp)) / 3600 as hour_diff
from cte t1 
join cte t2
    on t1.cust_id = t2.cust_id
    and t1.state = 1  -- Enter state
    and t2.state = 0  -- Exit state
    and t1.rn + 1 = t2.rn  -- Match consecutive states
group by 1;
