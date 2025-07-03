# 100 Days of LeetCode - Day 73

## 1. Merge Sorted Array (Python)

### Problem Description

You are given two sorted integer arrays `nums1` and `nums2`, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2`, respectively. Merge `nums2` into `nums1` as one sorted array **in-place**.

### ✅ Python Solution: Three Pointer (from end)

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1  # Last valid element index in nums1
        p2 = n - 1  # Last element index in nums2

        # Fill nums1 from the back
        for p in range(m + n - 1, -1, -1):
            if p2 < 0:
                break  # If nums2 is exhausted, we're done
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]  # Place larger of the two at current position
                p1 -= 1
            else:
                nums1[p] = nums2[p2]  # Place from nums2
                p2 -= 1
```

**Time Complexity:** `O(m + n)`
**Space Complexity:** `O(1)`  (in-place merge)

### Explanation:

The key idea is to merge from the back of the arrays to avoid overwriting values in `nums1`. We use two pointers `p1` and `p2` and insert elements from the end of `nums1`.

---

## 2. Monthly New vs Existing Users Share (SQL)

### Problem Description

Determine the monthly proportion of new users (first session in that month) versus existing users.

### ✅ SQL Solution

```sql
-- Step 1: Extract user_id and month of each session
with cte as (
    select distinct user_id, month(time_id) as user_month
    from fact_events
),

-- Step 2: Identify if user was active in previous month
cte2 as (
    select user_id, user_month,
           lag(user_month, 1) over(partition by user_id order by user_month asc) as prev_month
    from cte
)

-- Step 3: Calculate new vs existing users per month
select
    user_month as 'month',
    sum(case when prev_month is null then 1 else 0 end)/count(*) as share_new_users,
    sum(case when prev_month is not null then 1 else 0 end)/count(*) as share_existing_users
from cte2
group by 1
```

**Explanation:**

* Extract distinct (user, month) records.
* Use `LAG()` to check if the user appeared in the previous month.
* Aggregate by month to compute share of new vs existing users.

**Time Complexity:** `O(n log n)` (due to sorting in window function)
**Space Complexity:** `O(n)` (for intermediate CTEs)

---

## Challenge Progress

* **Day:** 73 / 100
* **Topic:** In-place Array Merge & Window Functions in SQL
* **Status:** ✅ Completed
