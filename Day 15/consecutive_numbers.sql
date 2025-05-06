### **Problem 180: Consecutive Numbers**


-- Use window functions to find 3 consecutive rows with same num
with cte as (
    select id, num, 
           lag(num, 1) over(order by id asc) as prev_num,  -- Previous row
           lead(num, 1) over(order by id asc) as next_num  -- Next row
    from Logs 
)

-- Check if current num equals both previous and next values
select distinct num as ConsecutiveNums
from cte
where prev_num = num and next_num = num;
