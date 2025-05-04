# 100 Days of LeetCode - Day 13

## 1. Container With Most Water (Python)

### Problem Description
Given `n` non-negative integers `height` where each represents a vertical line on the x-axis, find two lines that together with the x-axis forms a container that holds the most water.

### Solution 1: Brute Force

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                width = r - l
                area = max(area, min(height[l], height[r]) * width)

        return area
```

**Time Complexity:** `O(n^2)`  
**Space Complexity:** `O(1)`

### Solution 2: Two Pointer Approach

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0 , len(height) - 1 
        while l < r:
            length = r - l
            width = min(height[l], height[r])
            area = max(area, length * width)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

### Explanation
- The brute force method compares all possible pairs.
- The two-pointer method moves the pointer pointing to the shorter line inward to possibly find a container with greater height.


## 2. Immediate Delivery Percentage (SQL)

### Problem Description
Calculate the percentage of customers who received their first order on their preferred delivery date.

### Solution:

```sql
with first_orders as (
    select customer_id, min(order_date) as first_order
    from delivery
    group by 1
)

select ifnull(round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) /
                   (select count(*) from first_orders) * 100, 2), 0) as immediate_percentage
from delivery d
join first_orders o
on d.customer_id = o.customer_id
and d.order_date = o.first_order
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

### Explanation
- Use a CTE to get each customer's first order.
- Compare if the first order's date matches the preferred date.
- Compute and round the percentage of such cases.


## 3. Tweets With Too Many Characters (SQL)

### Problem Description
Find tweet IDs where the content exceeds 15 characters.

### Solution:

```sql
select tweet_id 
from tweets
where length(content) > 15
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

### Explanation
- Use `length()` to filter tweets with content longer than 15 characters.


## Challenge Progress

- **Day:** 13 / 100  
- **Topic:** Two Pointer & SQL Filtering  
- **Status:** ✅ Completed

