# 100 Days of LeetCode - Day 10

## 1. Valid Palindrome (Python)

### Problem Description  
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

---

### ✅ Solution 1: Using reverse string matching

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # Convert string to lowercase to make comparison case-insensitive
        t = []
        
        for i in s:
            if i.isalnum():  # Keep only alphanumeric characters
                t.append(i)
        
        t = ''.join(t)  # Join the characters into a single string
        return t == t[::-1]  # Check if the cleaned string is equal to its reverse
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

---

### ✅ Solution 2: Two-pointer Approach (In-place)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # Convert to lowercase
        l, r = 0, len(s) - 1  # Initialize two pointers

        while l < r:
            while l < r and not s[l].isalnum():  # Skip non-alphanumeric characters from left
                l += 1
            while l < r and not s[r].isalnum():  # Skip non-alphanumeric characters from right
                r -= 1
            
            if s[l] != s[r]:  # If characters don't match, return False
                return False
            
            l += 1
            r -= 1
        
        return True  # String is a valid palindrome
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

## 2. Swap Seats (SQL)

### Problem Description  
Write a query to swap the seat ID of every two students. If there is an odd number of students, the last one stays in place.

---

### ✅ Solution:

```sql
-- Swap seat IDs in pairs; last one remains the same if no pair exists
select 
    (case 
        when id % 2 = 0 then id - 1  -- Even ID: swap with previous
        when id % 2 != 0 and id = (select max(id) from seat) then id  -- Last odd ID: stay in place
        else id + 1  -- Odd ID: swap with next
     end) as id,
    student
from seat
order by 1 asc;
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

## 3. Employees Earning More Than Their Managers (SQL)

### Problem Description  
Find the employees who earn more than their manager.

---

### ✅ Solution:

```sql
-- Join employee with their manager and filter where employee salary is higher
select e.name as employee 
from employee e 
join employee m on e.managerId = m.id
where e.salary > m.salary;
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

## Challenge Progress

- **Day:** 10 / 100  
- **Topic:** Strings, Two Pointers, SQL Joins  
- **Status:** ✅ Completed