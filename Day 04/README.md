# 100 Days of LeetCode - Day 04

## 1. Group Anagrams (Python)

### Problem Description
Given an array of strings `strs`, group the anagrams together.  
Return a list of groups, where each group contains strings that are anagrams of each other.

### Solution: Using defaultdict with sorted keys

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict to group words by their sorted character key
        ans = defaultdict(list)

        for word in strs:
            # Sort the word and use it as the key
            sorted_word = ''.join(sorted(word))
            # Append the original word to the corresponding group
            ans[sorted_word].append(word)

        # Return all grouped anagrams as a list of lists
        return list(ans.values())
```

**Time Complexity:** `O(n * k log k)`  
**Space Complexity:** `O(n * k)`  
*Where `n` is the number of words and `k` is the average length of a word.*

### Explanation
- Anagrams share the same sorted form (e.g., "eat" and "tea" both become "aet").
- Use `defaultdict(list)` to group all words with the same sorted key.
- Return the grouped lists as output.



## 2. Article Views I (SQL)

### Problem Description
Find all authors who viewed their own articles.

### Solution:

```sql
-- Select unique authors who viewed their own articles
select distinct author_id as id
from views 
where author_id = viewer_id  -- author viewed their own article
order by 1                   -- order by id (ascending)
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`  

### Explanation
- `author_id = viewer_id` checks if the viewer and the author are the same.
- `distinct` ensures no duplicates.
- Sorted by `id` in ascending order.



## 3. Article Views II (SQL)

### Problem Description
Find the IDs of users who viewed more than one article on the same day.

### Solution:

```sql
-- Use CTE to remove duplicate rows from the views table
with cte as (
    select distinct * from views
)
-- Select viewers who viewed more than one article on the same day
select distinct viewer_id as id
from cte 
group by viewer_id, view_date  -- group by viewer and date
having count(*) > 1            -- keep only those with more than 1 view per day
order by 1                     -- order by id (ascending)
```

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)`  

### Explanation
- The CTE (`cte`) removes duplicate view records.
- We group the data by `viewer_id` and `view_date` to count how many views each user made per day.
- The `HAVING` clause filters out users with only one view.



## Challenge Progress

- **Day:** 04 / 100  
- **Topic:** Hashing & SQL Aggregation  
- **Status:** ✅ Completed