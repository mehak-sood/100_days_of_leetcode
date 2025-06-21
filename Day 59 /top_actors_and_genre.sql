-- Step 1: Count how many times each actor appeared in each genre and compute their avg rating
with most_frequent_genre as (
    select 
        actor_name, 
        genre, 
        count(*) as appearance_count,
        avg(movie_rating) as avg_rating,
        -- Rank genres for each actor by frequency and average rating (if frequency ties)
        dense_rank() over(
            partition by actor_name 
            order by count(*) desc, avg(movie_rating) desc
        ) as rnk
    from top_actors_rating
    group by 1, 2
),

-- Step 2: Among most frequent genres, rank actors by their genre's average rating
top_actor as (
    select *, 
        dense_rank() over(order by avg_rating desc) as rnk2
    from most_frequent_genre
    where rnk = 1  -- Keep only the most frequent genre per actor
)

-- Step 3: Output top 3 actors with the best average ratings in their most frequent genre
select actor_name, genre, avg_rating
from top_actor
where rnk2 <= 3
