### **Problem 1581: Customer who visited but did not make any transactions**

-- Find customers who visited but made no transaction
select v.customer_id, count(v.visit_id) as count_no_trans
from visits v
left join transactions t 
on v.visit_id = t.visit_id  -- Join on visit ID
where t.visit_id is null    -- Keep only visits with no matching transaction
group by 1;                 -- Group by customer_id
