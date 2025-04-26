### **Problem 595: Big Countries**

-- Select countries with either large population or large area
select name, population, area
from world
where population >= 25000000  -- countries with 25 million or more people
or area >= 3000000;           -- or area greater than or equal to 3 million sq km