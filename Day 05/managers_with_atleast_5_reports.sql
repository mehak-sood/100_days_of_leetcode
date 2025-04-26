### **Problem 570: Managers with Atleast 5 direct reports**

-- Select managers who have at least 5 direct reports
select m.name 
from employee m 
join employee e
on e.managerId = m.id        -- join employees to their managers
group by m.id                -- group by manager id
having count(*) >= 5;        -- only include those with 5 or more direct reports