-- First CTE: Calculate percentage of call-related events for each user
with cte as (
  select user_id,
    -- Count how many events are calls out of total events and convert to percentage
    sum(case when event_type in ('video call received', 'video call sent', 'voice call received', 'voice call sent') then 1 else 0 end) 
    / count(*) * 100 as perc
  from fact_events
  group by 1
  having perc >= 50  -- Only keep users where 50% or more of events are calls
)

-- Main query: Find client(s) with the highest number of events among these users
select client_id 
from (
  select client_id,
         dense_rank() over(order by count(*) desc) as rnk  -- Rank clients by event count (descending)
  from fact_events
  where user_id in (select user_id from cte)  -- Filter events only from high-call users
  group by 1
) a
where rnk = 1  -- Select top-ranked client(s) only
