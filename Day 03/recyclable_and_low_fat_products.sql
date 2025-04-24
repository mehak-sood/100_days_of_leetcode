#### **Problem 1757:**

-- Select product IDs where the product is both low fat and recyclable
select product_id
from products 
where low_fats = 'Y'
and recyclable = 'Y'