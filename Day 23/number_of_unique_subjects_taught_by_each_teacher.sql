### **Problem 2356: Number of Unique Subjects Taught by Each Teacher**

-- Count the number of unique subjects taught by each teacher
select teacher_id, count(distinct subject_id) as cnt
from teacher
group by 1;
