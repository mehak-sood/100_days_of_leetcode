#### **Problem 584:**

-- Select names of customers who do not have referee_id = 2, or have no referee
select name 
from customer 
where referee_id <> 2
or referee_id is null


