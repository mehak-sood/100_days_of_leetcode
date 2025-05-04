
# 100 Days of LeetCode - Day 11

## 1. Two Sum II - Input Array Is Sorted (Python)

### Problem Description
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number.

### Solution: Two Pointer Approach

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at the start and end of the list
        l, r = 0, len(numbers) - 1 

        while l < r:
            # If the current sum is greater than target, move right pointer left
            if numbers[l] + numbers[r] > target:
                r -= 1 
            # If the current sum is less than target, move left pointer right
            elif numbers[l] + numbers[r] < target:
                l += 1 
            else:
                # Return 1-based indices if sum matches the target
                return [l + 1, r + 1]
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`  

---

## 2. First Year Sales of Each Product (SQL)

### Problem Description
Report the product_id, first_year it was sold, quantity, and price in its first year of sale.

### Solution:

```sql
-- Use CTE to find the first year each product was sold
with first_year as (
    select product_id, min(year) as first_year
    from sales
    group by 1
)

-- Join with original sales table to get quantity and price for first year
select s.product_id, first_year, quantity, price
from sales s
join first_year f
on s.product_id = f.product_id
and s.year = f.first_year
```

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)`  

---

## 3. Confirmation Rate (SQL)

### Problem Description
Calculate the confirmation rate for each user.

### Solution:

```sql
-- Calculate confirmation rate for each user
select s.user_id,
-- Use CASE to count 'confirmed' actions and divide by total actions, rounded to 2 decimals
round(
    ifnull(
        sum(case when action = 'confirmed' then 1 else 0 end) / count(*),
        0
    ), 2
) as confirmation_rate
from signups s 
left join confirmations c
on s.user_id = c.user_id
group by 1
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`  

---

## Challenge Progress

- **Day:** 11 / 100  
- **Topic:** Two Pointers & SQL Joins  
- **Status:** ✅ Completed
