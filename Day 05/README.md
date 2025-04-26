# 100 Days of LeetCode - Day 05

## 1. Top K Frequent Elements (Python)

### Problem Description
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.  
You may return the answer in **any order**.


### Solution 1: Brute Force with Sorting

```python
from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency hashmap to count occurrences of each number
        freq_map = collections.defaultdict(int)
        for i in nums:
            freq_map[i] += 1

        # Convert the freq hashmap into a list of [frequency, number] pairs
        freq_list = [[value, key] for key, value in freq_map.items()]

        # Sort the list in descending order based on frequency
        sorted_list = sorted(freq_list, key=lambda x: x[0], reverse=True)

        # Collect the top k elements based on highest frequency
        ans = []
        for i in range(k):
            ans.append(sorted_list[i][1])
        
        return ans
```

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)`


### Solution 2: Min-Heap

```python
from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_heap = []

        # Quick return if we want all elements
        if k == len(nums):
            return nums 

        # Count frequencies of each number
        count = Counter(nums)  

        for key, value in count.items():
            # Push (frequency, number) into the min-heap
            heapq.heappush(freq_heap, (value, key))
            # Keep the heap size at most k by popping the smallest frequency
            if len(freq_heap) > k:
                heapq.heappop(freq_heap)

        # Extract just the numbers from the heap
        return [key for value, key in freq_heap]
```

**Time Complexity:** `O(n log k)`  
**Space Complexity:** `O(n)`

### Explanation
- The brute force approach builds a frequency map, sorts it, and returns the top `k` elements.
- The heap approach maintains a size-`k` min-heap of the most frequent items for more efficiency.



## 2. World Population and Area (SQL)

### Problem Description
Find all countries where the population is at least 25 million or the area is at least 3 million square km.

### Solution:

```sql
-- Select countries with either large population or large area
select name, population, area
from world
where population >= 25000000  -- countries with 25 million or more people
or area >= 3000000;        -- or area greater than or equal to 3 million sq km
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

### Explanation
- This query filters rows using a simple `WHERE` clause with `OR` logic.



## 3. Managers with At Least 5 Direct Reports (SQL)

### Problem Description
Find the names of employees who are managers of at least 5 other employees.

### Solution:

```sql
-- Select managers who have at least 5 direct reports
select m.name 
from employee m 
join employee e
on e.managerId = m.id        -- join employees to their managers
group by m.id                -- group by manager id
having count(*) >= 5;        -- only include those with 5 or more direct reports
```

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)`

### Explanation
- This query performs a self join to connect employees with their managers, then groups by manager and filters on the count.


## Challenge Progress

- **Day:** 05 / 100  
- **Topic:** Heaps & SQL Filtering  
- **Status:** ✅ Completed