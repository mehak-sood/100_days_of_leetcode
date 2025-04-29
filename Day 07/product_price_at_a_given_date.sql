### **Problem 1164: Product Price at a Given Date**

-- Find the price of each product on 2019-08-16
with cte as (
    select product_id, new_price, change_date
    from products
    where change_date <= '2019-08-16'   -- Consider only prices before or on the target date
),
cte2 as (
    select product_id, max(change_date) as last_change_date
    from cte
    group by 1                          -- Get the latest price change per product
),
cte3 as (
    select product_id, new_price
    from cte 
    where (product_id, change_date) in (select * from cte2) -- Match to latest price change
)

select p.product_id, ifnull(new_price, 10) as price   -- If no price found, default to 10
from (select distinct product_id from products) p
left join cte3
on p.product_id = cte3.product_id;
