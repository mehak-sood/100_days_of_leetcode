
# 100 Days of LeetCode - Day 15

## 1. Best Time to Buy and Sell Stock (Python)

### Problem Description  
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If no profit is possible, return `0`.

### ✅ Solution 1: Brute Force (O(n²) Time)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # Iterate through all pairs (buy i, sell j)
        for i in range(len(prices) - 1):  # Choose buy day
            for j in range(i + 1, len(prices)):  # Choose sell day
                profit = prices[j] - prices[i]  # Calculate profit
                max_profit = max(max_profit, profit)  # Update max profit if needed
        return max_profit  # Return the highest possible profit
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)


### ✅ Solution 2: One Pass (O(n) Time, O(1) Space)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        min_price = float('inf')  # Track the minimum price seen so far
        max_profit = float('-inf')  # Track the maximum profit found so far

        for p in prices:
            min_price = min(p, min_price)  # Update min price if current is lower
            profit = p - min_price  # Profit if selling today
            max_profit = max(profit, max_profit)  # Update max profit if today's is better

        return max_profit  # Return the best profit possible
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Explanation:**  
1. The Solution 1 tries every possible pair of buy and sell days and calculate the profit. Keep track of the maximum.
2. The Solution 2 tracks the lowest price so far and calculate the profit at each step. This avoids unnecessary comparisons.



## 2. Consecutive Numbers (SQL)

### Problem Description  
Write a SQL query to find all numbers that appear at least three times consecutively in a table.

### ✅ SQL Solution

```sql
-- Use window functions to find 3 consecutive rows with same num
with cte as (
    select id, num, 
           lag(num, 1) over(order by id asc) as prev_num,  -- Previous row
           lead(num, 1) over(order by id asc) as next_num  -- Next row
    from Logs 
)

-- Check if current num equals both previous and next values
select distinct num as ConsecutiveNums
from cte
where prev_num = num and next_num = num;
```

**Explanation:**  
Use `LAG` and `LEAD` to check for the same number in consecutive rows (before and after current row).

**Time Complexity:** O(n)  
**Space Complexity:** O(n) (due to CTE and window functions)


## 3. Triangle Judgement (SQL)

### Problem Description  
Write a SQL query to report for each row whether the given sides can form a valid triangle.


### ✅ SQL Solution

```sql
-- Check triangle validity using the triangle inequality theorem
select *, 
       (case 
           when x + y > z and y + z > x and x + z > y 
           then 'Yes'  -- Valid triangle
           else 'No'   -- Not a triangle
        end) as 'triangle'
from triangle;
```

**Explanation:**  
Applies the triangle inequality theorem to verify if the three sides can form a triangle.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## Challenge Progress

* **Day:** 15 / 100  
* **Topic:** Stock Profit + SQL Window Functions & Logic  
* **Status:** ✅ Completed
