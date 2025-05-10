### **Problem 620: Not Boring Movies**

-- Select all rows where:
-- - ID is odd (id % 2 != 0)
-- - Description is not 'boring'
-- Then sort by rating in descending order
select * 
from cinema
where id % 2 != 0
  and description != 'boring'
order by rating desc;
