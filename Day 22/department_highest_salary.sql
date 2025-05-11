### **Problem 184: Department Highest Salary**

-- Create a CTE to rank employees within each department by salary
with cte as (
    select name, salary, departmentId,
           dense_rank() over(partition by departmentId order by salary desc) as rnk
    from employee 
)

-- Join with department table and select top earners per department (rank = 1)
select d.name as department, cte.name as employee, salary
from cte 
join department d on cte.departmentId = d.id
where rnk = 1
