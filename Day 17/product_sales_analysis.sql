### **Problem 1068: Product Sales Analysis I**

-- Select product name, year, and price from sales and product tables
select product_name, year, price
from sales s
join product p
on s.product_id = p.product_id;
