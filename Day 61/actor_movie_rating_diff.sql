-- Step 1: Get the latest film release date for each actor
with cte as (
    select actor_name, max(release_date) as latest_film_release
    from actor_rating_shift
    group by 1
),

-- Step 2: Identify actors with only one film (skip rating difference calc)
t1 as (
    select actor_name
    from actor_rating_shift
    group by 1
    having count(*) = 1 
),

-- Step 3: Calculate the average rating excluding the most recent film
cte2 as (
    select actor_name, avg(film_rating) as avg_rating
    from actor_rating_shift
    where (actor_name, release_date) not in (select * from cte)  -- exclude latest film
       or actor_name in (select * from t1)  -- include all if actor has only one film
    group by 1
),

-- Step 4: Get the latest rating for each actor
cte3 as (
    select a.actor_name, film_rating as latest_rating 
    from actor_rating_shift a
    join cte b
    on a.actor_name = b.actor_name
    and a.release_date = b.latest_film_release
)

-- Step 5: Final output combining average and latest ratings
select a.actor_name, avg_rating, latest_rating, 
       (latest_rating - avg_rating) as rating_difference
from cte2 a
join cte3 b
on a.actor_name = b.actor_name
    