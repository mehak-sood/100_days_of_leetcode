### **Problem 175: Combine Two Tables**


-- Get personal and address information
select p.firstname, p.lastname, a.city, a.state
from person p
left join address a
on p.personId = a.personId;   -- Match person to address by personId
