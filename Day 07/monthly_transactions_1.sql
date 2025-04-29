### **Problem 1193: Monthly Transactions I**

-- Summarize transactions per month and country
select 
    left(trans_date, 7) as "month",         -- Extract the month part
    country,
    count(*) as trans_count,                -- Total transactions
    sum(case when state = 'approved' then 1 else 0 end) as approved_count,  -- Approved transactions
    sum(amount) as trans_total_amount,      -- Total transaction amount
    sum(case when state = 'approved' then amount else 0 end) as approved_total_amount  -- Total approved amount
from transactions 
group by 1, 2;                              -- Group by month and country
