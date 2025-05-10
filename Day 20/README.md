# 100 Days of LeetCode - Day 20

## Problem: Sliding Window Maximum (Leetcode 239)

### Problem Description

You are given an array of integers `nums`, and there is a sliding window of size `k` which moves from the very left to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the maximum in each window.


## Solutions

### Solution 1: Brute Force Approach

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return [max(nums)]  # If only one window, return its max

        l, r = 0, k - 1  # Initialize window pointers
        res = []  # Result list

        while r < len(nums):
            max_num = float('-inf')
            for i in range(l, r + 1):  # Traverse current window
                if nums[i] > max_num:
                    max_num = nums[i]
            res.append(max_num)  # Append max of current window
            l += 1  # Slide window
            r += 1

        return res
```

**Time Complexity:** `O(n * k)`
**Space Complexity:** `O(n)`

### Solution 2: Optimized Approach using Monotonic Queue

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Deque to store indices
        res = []

        # Initialize first window
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()  # Maintain decreasing order
            dq.append(i)

        res.append(nums[dq[0]])  # Max of first window

        # Process remaining elements
        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()  # Remove out-of-window index

            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()  # Remove smaller elements
            dq.append(i)

            res.append(nums[dq[0]])  # Append max of current window

        return res
```

**Time Complexity:** `O(n)`
**Space Complexity:** `O(k)`

### Explanation

* The brute-force method simply checks every window and finds the max manually.
* The optimized solution uses a **Decreasing Monotonic Queue**, where the largest value in the current window is always at the front of the queue.

  * Elements smaller than the incoming number are removed since they will never be the max.
  * This drastically reduces the number of operations.

### References

* [Monotonic Queue (GFG)](https://www.geeksforgeeks.org/introduction-to-monotonic-queues/)
* [Deque in Python (GFG)](https://www.geeksforgeeks.org/deque-in-python/)

---

## SQL Challenges

### SQL 1: Manager Reports Count and Average Age

```sql
with cte as (
    select reports_to as manager_id,
           count(*) as reports_count,
           round(avg(age), 0) as average_age
    from employees
    where reports_to is not null
    group by reports_to
)

select e.employee_id, e.name, reports_count, average_age
from cte
join employees e on cte.manager_id = e.employee_id
order by 1;
```

### SQL 2: Filter Non-Boring Movies with Odd IDs

```sql
select *
from cinema
where id % 2 != 0
  and description != 'boring'
order by rating desc;
```

---

## Challenge Progress

* **Day:** 20 / 100
* **Topic:** Sliding Window / Deques / SQL Joins & Filters
* **Status:** ✅ Completed
