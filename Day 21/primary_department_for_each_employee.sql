### **Problem 1789: Primary Department for Each Employee*

-- Select employees who either:
-- (1) have primary_flag = 'Y'
-- (2) OR appear only once in the table (meaning no ambiguity in departments)

select employee_id, department_id
from employee 
where primary_flag = 'Y'

union  -- Include both sets without duplicates

-- This subquery finds employees who appear only once, regardless of primary_flag
(select employee_id, department_id
 from employee 
 group by employee_id
 having count(*) = 1)
