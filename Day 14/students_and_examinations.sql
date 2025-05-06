### **Problem 1280: Students and Examinations**

-- CTE to create a cross join of all students with all subjects
with cte as (
    select s.student_id, s.student_name, subject_name
    from students s, subjects
)

-- Left join with exams table to count attended exams
select 
    s.student_id, 
    s.student_name, 
    s.subject_name, 
    count(e.subject_name) as attended_exams
from cte s 
left join examinations e
    on s.student_id = e.student_id
    and s.subject_name = e.subject_name
group by 1, 2, 3
order by 1, 3;
