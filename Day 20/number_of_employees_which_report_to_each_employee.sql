### **Problem 1731: The Number of Employees Which Report to Each Employee**

-- First, compute number of direct reports and average age per manager
with cte as (
    select 
        reports_to as manager_id,
        count(*) as reports_count,
        round(avg(age), 0) as average_age
    from employees
    where reports_to is not null  -- Only employees who report to someone
    group by reports_to
)

-- Join the manager info with employee table to get manager name
select 
    e.employee_id,
    e.name,
    cte.reports_count,
    cte.average_age
from cte
join employees e
on cte.manager_id = e.employee_id
order by e.employee_id;
