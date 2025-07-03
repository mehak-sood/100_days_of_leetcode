-- Step 1: Create a CTE to extract user_id and the month of their activity
with cte as (
    select distinct user_id, month(time_id) as user_month
    from fact_events
),

-- Step 2: Add previous month value per user to track continuity
cte2 as (
    select user_id, user_month, 
           lag(user_month, 1) over(partition by user_id order by user_month asc) as prev_month
    from cte
)

-- Step 3: Aggregate by month to compute new and existing user share
select 
    user_month as 'month',

    -- New user: first appearance in that month (no previous month)
    sum(case when prev_month is null then 1 else 0 end) / count(*) as share_new_users,

    -- Existing user: has a record in previous month
    sum(case when prev_month is not null then 1 else 0 end) / count(*) as share_existing_users

from cte2
group by 1
