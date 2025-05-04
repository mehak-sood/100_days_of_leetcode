### **Problem 181: Employees Earning More Than Their Managers**

-- Find employees who earn more than their managers
select e.name as employee 
from employee e 
join employee m 
on e.managerId = m.id  -- Join employee with their manager
where e.salary > m.salary;  -- Filter those who earn more than the manager
