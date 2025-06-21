# 100 Days of LeetCode - Day 60

## 1. Longest Common Prefix (Python)

### Problem Description

Write a function to find the longest common prefix string amongst an array of strings.  
If there is no common prefix, return an empty string `""`.

## Solutions

### Solution: Prefix Shrinking

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        pre = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(pre) != 0:
                pre = pre[0:len(pre)-1]
                if pre == "":
                    return ""
        return pre
```

**Time Complexity:** : O(N * M) where N is the number of strings and M is the length of the longest string.
**Space Complexity:** : O(1)

**Explanation:**

* The solution assumes the first string as the initial prefix.
* It checks every string to see if it starts with the current prefix.
* If not, the prefix is shortened one character at a time until it matches or becomes empty.
* Returns the longest valid prefix common to all strings.

## 2. SQL Problems

Problem 1: Consecutive User Activity (3 Days in a Row)
```sql
with cte as (
    select distinct user_id, record_date
    from sf_events
),
cte2 as (
    select user_id, record_date,
           lag(record_date,1) over(order by record_date asc) as prev_record,
           lead(record_date,1) over(order by record_date asc) as next_record
    from cte
)
select distinct user_id
from cte2
where datediff(record_date, prev_record) = 1
  and datediff(next_record, record_date) = 1;
```
**Explanation:**

* Cte removes duplicate activity records for each user.
* lag and lead are used to get the previous and next activity dates.
* The final filter selects users whose activity dates form a consecutive 3-day sequence.


## Challenge Progress

* **Day:** 60 / 100
* **Topic:** Strings & SQL Time-Series
* **Status:** ✅ Completed
