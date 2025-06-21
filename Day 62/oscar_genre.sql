-- First CTE: count how many times each nominee has won and rank them by wins
with cte as (
    select nominee, 
           count(*) as wins, 
           dense_rank() over(order by count(*) desc) as rnk
    from oscar_nominees
    where winner = 1
    group by 1
),

-- Second CTE: filter the top-ranked nominee(s) with the highest win count
cte2 as (
    select nominee 
    from cte
    where rnk = 1
)

-- Final query: find unique genres associated with the top-winning nominee(s)
select distinct top_genre
from nominee_information a
join cte2 b
    on a.name = b.nominee;
