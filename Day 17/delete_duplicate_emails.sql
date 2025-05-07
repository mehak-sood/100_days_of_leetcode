### **Problem 196: Delete Duplicate Emails**

-- Delete duplicate email entries, keeping only the one with the smallest ID
delete p1.*
from person p1
join person p2
on p1.email = p2.email
and p1.id > p2.id;

-- Joins the person table with itself (p1, p2) on duplicate emails.
-- Deletes the record (p1) with a higher id so that only the earliest instance remains.