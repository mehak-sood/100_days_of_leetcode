### **Problem 185: Department top three salaries**

-- Get the top 3 highest salaries in each department
with cte as (
    select 
        name, 
        salary, 
        departmentId,
        dense_rank() over(partition by departmentId order by salary desc) as rnk  -- Rank salaries within departments
    from employee
)
select 
    d.name as department, 
    e.name as employee, 
    e.salary
from cte e
join department d
on e.departmentId = d.id       -- Join employees with their departments
where e.rnk <= 3;              -- Only keep employees ranked top 3
