# 100 Days of LeetCode - Day 22

## 1. Min Stack (Python)

### Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

* `MinStack()` initializes the stack.
* `void push(int val)` pushes the element onto the stack.
* `void pop()` removes the element on the top.
* `int top()` gets the top element.
* `int getMin()` retrieves the minimum element.

## Solutions

### Solution 1: Tuple-Based Stack

```python
class MinStack:

    def __init__(self):
        # Stack stores tuples of (value, current_min)
        self.stack = []    

    def push(self, val: int) -> None:
        if not self.stack:
            # If empty, val is also the current min
            self.stack.append((val,val))
            return
        # Track current min while pushing new value
        current_min = self.stack[-1][1]
        self.stack.append((val, min(val,current_min)))

    def pop(self) -> None:
        # Pop the top tuple
        self.stack.pop()

    def top(self) -> int:
        # Return the value from top tuple
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the current min from top tuple
        return self.stack[-1][1]
```

**Time Complexity:** O(1) for all operations
**Space Complexity:** O(n) to store (value, min) tuples

### Solution 2: Two Stacks

```python
class MinStack:

    def __init__(self):
        self.stack = []         # Stack to hold values
        self.min_stack = []     # Stack to hold minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push val to min_stack if it's smaller or stack is empty
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop from min_stack if it's the current min
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

**Time Complexity:** O(1) for all operations
**Space Complexity:** O(n) for two stacks

---

## 2. SQL Problems

### Problem 1: Department Top Earners

```sql
with cte as (
    select name, salary, departmentId,
           dense_rank() over(partition by departmentId order by salary desc) as rnk
    from employee
)

select d.name as department, cte.name as employee, salary
from cte
join department d on cte.departmentId = d.id
where rnk = 1
```

**Explanation:**

* Uses `dense_rank` to rank employees by salary in each department.
* Filters to top earners (`rnk = 1`).
* Joins with department to fetch department name.

### Problem 2: Customers Without Orders

```sql
select name as customers
from customers c
left join orders o on c.id = o.customerId
where o.id is null
```

**Explanation:**

* `LEFT JOIN` includes all customers, whether or not they have orders.
* The `where o.id is null` condition filters those with **no matching orders**.

---

## Challenge Progress

* **Day:** 22 / 100
* **Topic:** Stack Design & SQL Joins
* **Status:** ✅ Completed
