-- Step 1: Create a CTE of distinct completed trips per driver and date
with cte as (
    select distinct driver_id, trip_date
    from uber_trips
    where is_completed = 1
)

-- Step 2: Join the CTE to itself to find drivers with trips in two consecutive months
select distinct t1.driver_id
from cte t1
join cte t2
    on t1.driver_id = t2.driver_id  -- Same driver
    -- Check if t2's trip is in the month immediately after t1's trip
    and date_format(date_add(t1.trip_date, interval 1 month), '%Y%m') = date_format(t2.trip_date, '%Y%m')
