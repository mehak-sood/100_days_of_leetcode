### **Problem 610: Triangle Judgement**

-- Check triangle validity using the triangle inequality theorem
select *, 
       (case 
           when x + y > z and y + z > x and x + z > y 
           then 'Yes'  -- Valid triangle
           else 'No'   -- Not a triangle
        end) as 'triangle'
from triangle;
