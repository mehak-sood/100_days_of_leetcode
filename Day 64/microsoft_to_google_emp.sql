-- Create a CTE to compare current and previous employer per user based on start date
with cte as (
    select 
        user_id, 
        employer, 
        lag(employer, 1) over(
            partition by user_id 
            order by start_date asc
        ) as prev_employer  -- Gets the employer immediately before current one
    from linkedin_users
)

-- Count number of users whose current employer is Google
-- and immediately previous employer was Microsoft
select count(user_id)
from cte
where employer = 'Google'
  and prev_employer = 'Microsoft';
