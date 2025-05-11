# 100 Days of LeetCode - Day 21

## 1. Valid Parentheses (Python)

### Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid. A string is valid if:

* Open brackets are closed by the same type of brackets.
* Open brackets are closed in the correct order.

### Solution: Stack Approach

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        paran_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []  # Stack to keep track of opening brackets

        for i in s:
            if i in paran_map:
                # Pop the top of the stack if not empty, otherwise use a dummy char
                top = stack.pop() if stack else '#'

                # If the popped element does not match the expected opening bracket, return False
                if paran_map[i] != top:
                    return False
            else:
                # If it's an opening bracket, push it to the stack
                stack.append(i)

        # If the stack is empty, all brackets were matched correctly
        return not stack
```

**Time Complexity:** `O(n)`
**Space Complexity:** `O(n)`

### Explanation

* This approach uses a stack to match each opening bracket with its correct closing counterpart.
* We maintain a dictionary `paran_map` that maps closing brackets to their opening pair.
* If we find a closing bracket, we check if the top of the stack matches; otherwise, we return `False`.
* At the end, if the stack is empty, the parentheses are valid.

---

## 2. SQL Problems

### Problem 1: Return Employee's Department if They Have Primary Flag = 'Y' or Only One Record

```sql
-- Select employees who either:
-- (1) have primary_flag = 'Y'
-- (2) OR appear only once in the table (no ambiguity)

select employee_id, department_id
from employee
where primary_flag = 'Y'

union  -- Include both sets without duplicates

-- This subquery finds employees who appear only once
(select employee_id, department_id
 from employee
 group by employee_id
 having count(*) = 1);
```

### Problem 2: Get the Nth Highest Salary

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      -- Use a CTE to assign dense ranks to salaries in descending order
      with cte as (
          select salary,
                 dense_rank() over(order by salary desc) as rnk
          from employee
      )

      -- Select the salary where the rank matches N
      select distinct salary
      from cte
      where rnk = N
  );
END
```

### Explanation

* **Primary Flag Query**: Selects employees based on either having a unique entry or a designated primary department.
* **Nth Salary Query**: Uses a window function (`DENSE_RANK`) to return the Nth highest salary.

---

## Challenge Progress

* **Day:** 21 / 100
* **Topics:** Stack (Python), SQL (Filtering, Window Functions)
* **Status:** ✅ Completed
