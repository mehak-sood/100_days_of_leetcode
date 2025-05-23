# 100 Days of LeetCode - Day 23

## 1. Evaluate Reverse Polish Notation (Python)

### Problem Description

Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN). Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

## Solutions

### Solution: Stack-Based Evaluation

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Stack to store operands

        for token in tokens:
            # If the token is an operator, pop two operands and apply the operation
            if token in {'+', '-', '*', '/'}:
                y = stack.pop()  # Second operand
                x = stack.pop()  # First operand

                if token == '+':
                    stack.append(x + y)
                elif token == '-':
                    stack.append(x - y)
                elif token == '*':
                    stack.append(x * y)
                elif token == '/':
                    # Perform integer division that truncates toward zero
                    stack.append(int(x / y))
            else:
                # If the token is a number, convert to int and push to stack
                stack.append(int(token))

        return stack[0]  # Final result is the only item left on the stack
```

**Time Complexity:** `O(n)`
**Space Complexity:** `O(n)`

### Explanation

* A stack is used to evaluate Reverse Polish Notation (RPN) expressions.
* When a number is encountered, it's pushed onto the stack.
* When an operator is encountered, two operands are popped, and the result is pushed back.
* The final result remains on the top of the stack.

---

## 2. SQL Queries

### Problem 1: Employees with Salary < 30000 and No Manager in the Company

```sql
select employee_id
from employees
where salary < 30000
and manager_id not in (
    select employee_id from employees )
order by 1 asc;
```

### Explanation

* Finds employees earning less than 30000.
* Filters out those whose manager\_id exists in the company.
* `manager_id not in (...)` ensures no manager is listed in the employees table.

---

### Problem 2: Count of Unique Subjects per Teacher

```sql
select teacher_id, count(distinct subject_id) as cnt
from teacher
group by 1;
```

### Explanation

* Counts distinct `subject_id`s taught by each `teacher_id`.
* Groups the result by `teacher_id`.

---

## Challenge Progress

* **Day:** 23 / 100
* **Topic:** Stack Implementation in Python & Aggregate SQL Queries
* **Status:** ✅ Completed
