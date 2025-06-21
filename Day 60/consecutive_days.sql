-- Create a CTE to get unique combinations of user_id and their activity date
with cte as (
    select distinct user_id, record_date
    from sf_events
),

-- Add previous and next record_date for each user using window functions
cte2 as (
    select 
        user_id, 
        record_date,
        lag(record_date, 1) over(order by record_date asc) as prev_record, -- Previous date
        lead(record_date, 1) over(order by record_date asc) as next_record -- Next date
    from cte
)

-- Final selection: users who have three consecutive activity days
select distinct user_id
from cte2
where datediff(record_date, prev_record) = 1 -- Yesterday
  and datediff(next_record, record_date) = 1 -- Tomorrow
