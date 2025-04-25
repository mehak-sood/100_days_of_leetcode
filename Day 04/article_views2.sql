### **Problem 1149: Article Views 2**

-- Use CTE to remove duplicate rows from the views table
with cte as (
    select distinct * from views
)
-- Select viewers who viewed more than one article on the same day
select distinct viewer_id as id
from cte 
group by viewer_id, view_date  -- group by viewer and date
having count(*) > 1            -- keep only those with more than 1 view per day
order by 1                     -- order by id (ascending)   
