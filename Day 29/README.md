# 100 Days of LeetCode - Day 29

## 1. Search a 2D Matrix (Python)

### Problem Description
Write an efficient algorithm that searches for a value in an `m x n` matrix.  
This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

### ✅ Solution: Binary Search on Flattened Matrix

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # Number of rows

        if m == 0:
            return False  # Return False if matrix is empty

        n = len(matrix[0])  # Number of columns

        # Treat the 2D matrix as a 1D array for binary search
        l, r = 0, m * n - 1

        while l <= r:
            pivot_idx = (l + r) // 2  # Middle index in 1D flattened matrix
            # Convert 1D index to 2D coordinates
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]

            if target == pivot_element:
                return True  # Found the target
            elif target < pivot_element:
                r = pivot_idx - 1  # Search left half
            else:
                l = pivot_idx + 1  # Search right half

        return False  # Target not found
```

**Time Complexity:** `O(log(m*n))`  
**Space Complexity:** `O(1)`

---

## 2. Most Expensive and Cheapest Wine with Ties (SQL)

### Problem Description  
Find the cheapest and the most expensive variety in each region. Output the region along with the corresponding most expensive and the cheapest variety. Be aware that there are 2 region columns, the price from that row applies to both of them.

Note: The results set contains ties, so your solution should account for this.

For example in the event of a tie for the cheapest wine your output should look similar to this:

region             | most_expensive_variety | cheapest_variety
region_name | expensive_variety             | cheap_variety_1
region_name | expensive_variety             | cheap_variety_2

### ✅ SQL Solution:

```sql
-- Combine region_1 and region_2 data into one column
with cte as (
    select region_1 as region, variety, price from winemag_pd
    union all 
    select region_2, variety, price from winemag_pd
),

-- For each region, find the min and max wine price
cte2 as (
    select region, min(price) as cheapest, max(price) as expensive
    from cte
    group by 1
),

-- Find varieties that are the most expensive per region (with ties)
cte4 as (
    select distinct t.region, t.variety as most_expensive_variety
    from cte t
    join cte2 t2
    on t.region = t2.region 
    and t.price = t2.expensive
),

-- Find varieties that are the cheapest per region (with ties)
cte5 as (
    select distinct t.region, t.variety as cheapest_variety
    from cte t
    join cte2 t3
    on t.region = t3.region 
    and t.price = t3.cheapest
)

-- Join both to show both most expensive and cheapest varieties per region
select distinct cte4.region, most_expensive_variety, cheapest_variety
from cte4 
join cte5 on cte4.region = cte5.region
order by 1 desc;
```

---

## 3. Customer Tracking (SQL)

### Problem Description  
Given the users' sessions logs on a particular day, calculate how many hours each user was active that day.

Note: The session starts when state=1 and ends when state=0.

### ✅ SQL Solution:

```sql
-- Number the customer's tracking states by time order
with cte as (
    select *, row_number() over(partition by cust_id order by timestamp asc) as rn
    from cust_tracking
)

-- Join each 'entry' state with the immediately next 'exit' state for the same customer
select 
    t1.cust_id, 
    -- Calculate time spent in seconds, divide by 3600 to convert to hours
    sum(timestampdiff(second, t1.timestamp, t2.timestamp)) / 3600 as hour_diff
from cte t1 
join cte t2
    on t1.cust_id = t2.cust_id
    and t1.state = 1  -- Enter state
    and t2.state = 0  -- Exit state
    and t1.rn + 1 = t2.rn  -- Match consecutive states
group by 1;
```

---

## Challenge Progress

- **Day:** 29 / 100  
- **Topic:** Binary Search & SQL Joins with Time Logic  
- **Status:** ✅ Completed