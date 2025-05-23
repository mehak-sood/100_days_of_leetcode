### **Problem 1978: Employees Whose Manager Left the Company*

-- Select employee IDs for those with salary < 30000
-- and whose manager_id is NOT present in the employees table
select employee_id 
from employees 
where salary < 30000
and manager_id not in (
    select employee_id from employees
)
order by 1 asc;
