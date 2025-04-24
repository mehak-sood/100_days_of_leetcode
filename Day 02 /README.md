# 100 Days of LeetCode - Day 02

## 1. Contains Duplicate (Python)

### Problem Description
Given an array of integers, determine if any value appears at least twice.  
Return `True` if any value appears more than once, and `False` if every element is distinct.

## Solution

### Solution 1: Using Set

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert the list to a set to remove duplicates.
        # If the length of the set is less than the original list, duplicates were removed.
        if len(nums) == len(set(nums)):
            return False  # No duplicates found
        return True       # Duplicates found
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`  
*Reason: Creating a set takes linear space and time proportional to the number of elements.*


### Solution 2: Using Dictionary

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty dictionary to store the frequency of each number
        freq_map = {}
        for i in nums:
            # If the number is already in the dictionary, it means it's a duplicate
            if i in freq_map:
                return True
            else:
                # Otherwise, add the number to the dictionary
                freq_map[i] = 1
        return False  # No duplicates found
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`  
*Reason: A dictionary is used to store each element seen once, requiring linear space.*

### Explanation
1. For Approach 1, we use the properties of set to remove the duplicates. Convert list to a set and check the length of the list and set. If the length of list is same as the set, that means there were no duplicates and return False. Otherwise return True
2. For Approach 2, We use a hash map (dictionary) to store each number's value as a key and its frequency as the value. If the num is already in the dictionary return True else add the num to the dictionary. 

## 2. Weather Data Analysis (SQL)
### Problem Description
From a table of daily temperatures, find the ids of days where the temperature was higher than the previous day.

### Solution 1: Using CTE and Window Functions

```sql
WITH cte AS (
    SELECT 
        id, 
        recordDate, 
        temperature,
        -- Get the previous day's recordDate using lag function
        LAG(recordDate, 1) OVER(ORDER BY recordDate ASC) AS prev_date,
        -- Get the previous day's temperature using lag function
        LAG(temperature, 1) OVER(ORDER BY recordDate ASC) AS prev_temp
    FROM weather
)
SELECT id
FROM cte
-- Check if the current record is exactly one day after the previous record
-- and the temperature has increased
WHERE DATEDIFF(recordDate, prev_date) = 1
  AND temperature > prev_temp;
```

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)`  
*Reason: Sorting for window function (`ORDER BY`) dominates; CTE holds intermediate data.*

### Solution 2: Using Self Join

```sql
SELECT w1.id
FROM weather w1 
JOIN weather w2
  -- Join on records that are one day apart
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
  -- Ensure the temperature of the current day is higher than the previous day
  AND w1.temperature > w2.temperature;
```

**Time Complexity:** `O(n^2)`  
**Space Complexity:** `O(1)`  
*Reason: Self join compares every record with every other, unless indexed appropriately.*

### Explanation
1. The Solution 1 uses the LAG() function to fetch the previous day's data for each row and compares it to the current day. It checks if the temperature has increased and if the records are one day apart.
2. For Solution 2 joins the weather table with itself to compare each day's record to the previous day's record, ensuring the temperatures are higher and the dates are exactly one day apart.

## Challenge Progress

- **Day:** 02 / 100  
- **Topic:** Arrays & SQL Joins  
- **Status:** ✅ Completed  




