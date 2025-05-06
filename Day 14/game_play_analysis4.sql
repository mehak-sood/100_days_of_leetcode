### **Problem 550: Game Play Analysis IV**

-- CTE to get each player's first login date
with first_login as (
    select player_id, min(event_date) as first_login
    from activity 
    group by player_id
)

-- Count how many players returned the next day
select ifnull(
    round(
        count(distinct f.player_id) / count(distinct a.player_id), 2
    ), 
0) as fraction
from activity a 
left join first_login f
    on a.player_id = f.player_id
    and datediff(a.event_date, f.first_login) = 1  -- returned the next day
