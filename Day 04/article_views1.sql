### **Problem 1148: Article Views 1**


-- Select unique authors who viewed their own articles
select distinct author_id as id
from views 
where author_id = viewer_id  -- author viewed their own article
order by 1                   -- order by id (ascending)
