### **Problem 182: Duplicate Emails**

-- Find all emails that appear more than once in the Person table

SELECT DISTINCT p1.email
FROM person p1
JOIN person p2
  ON p1.email = p2.email  -- Same email
 AND p1.id <> p2.id       -- But different person (avoid self-join match)
