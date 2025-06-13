-- Combine region_1 and region_2 data into one column
with cte as (
    select region_1 as region, variety, price from winemag_pd
    union all 
    select region_2, variety, price from winemag_pd
),

-- For each region, find the min and max wine price
cte2 as (
    select region, min(price) as cheapest, max(price) as expensive
    from cte
    group by 1
),

-- Find varieties that are the most expensive per region (with ties)
cte4 as (
    select distinct t.region, t.variety as most_expensive_variety
    from cte t
    join cte2 t2
    on t.region = t2.region 
    and t.price = t2.expensive
),

-- Find varieties that are the cheapest per region (with ties)
cte5 as (
    select distinct t.region, t.variety as cheapest_variety
    from cte t
    join cte2 t3
    on t.region = t3.region 
    and t.price = t3.cheapest
)

-- Join both to show both most expensive and cheapest varieties per region
select distinct cte4.region, most_expensive_variety, cheapest_variety
from cte4 
join cte5 on cte4.region = cte5.region
order by 1 desc;
