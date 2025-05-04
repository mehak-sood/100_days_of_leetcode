### **Problem 1070: Product Sales Analysis III**

-- Use CTE to find the first year each product was sold
with first_year as (
    select product_id, min(year) as first_year
    from sales
    group by 1
)

-- Join with original sales table to get quantity and price for first year
select s.product_id, first_year, quantity, price
from sales s
join first_year f
on s.product_id = f.product_id
and s.year = f.first_year
