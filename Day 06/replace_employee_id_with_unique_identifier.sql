### **Problem 1378: Replace Employee ID With The Unique Identifier**

-- Map employees to their unique IDs
select u.unique_id, e.name
from employees e
left join employeeUNI u
on e.id = u.id;   -- Match by employee id
