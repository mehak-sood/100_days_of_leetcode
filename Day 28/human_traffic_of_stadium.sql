### **Problem 601: Human Traffic of Stadium*

-- Step 1: Create a CTE with a row number to identify consecutive records
with cte as (
    select *, 
           row_number() over(order by id asc) as rn
    from Stadium
    where people >= 100  -- filter only rows with at least 100 people
),

-- Step 2: Create a group identifier by subtracting row_number from the id
cte2 as (
    select id, visit_date, people, (id - rn) as grp
    from cte
),

-- Step 3: Find groups that have at least 3 consecutive days
cte3 as (
    select grp
    from cte2
    group by grp
    having count(*) >= 3
)

-- Final result: fetch rows that belong to those qualifying groups
select id, visit_date, people
from cte2 
where grp in (select grp from cte3)
order by visit_date asc
