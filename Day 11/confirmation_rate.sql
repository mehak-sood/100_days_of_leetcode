### **Problem 1934: Confirmation rate**

-- Calculate confirmation rate for each user
select s.user_id,
-- Use CASE to count 'confirmed' actions and divide by total actions, rounded to 2 decimals
round(
    ifnull(
        sum(case when action = 'confirmed' then 1 else 0 end) / count(*),
        0
    ), 2
) as confirmation_rate
from signups s 
left join confirmations c
on s.user_id = c.user_id
group by 1
