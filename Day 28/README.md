# 100 Days of LeetCode - Day 28

## ✅ Problems Covered:
- **704. Binary Search** (Python)
- **Stadium Attendance** (SQL)
- **First Login per Player** (SQL)

---

## 1. 🔍 Binary Search (Python)

### Problem Statement:
Given a sorted array of integers `nums` and an integer `target`, return the index if the target is found. If not, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

### Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers to the start and end of the array
        l, r = 0, len(nums) - 1

        # Continue searching while the left pointer does not cross the right
        while l <= r:
            # Calculate the middle index
            mid = (l + r) // 2

            # If the middle element is greater than target, search left half
            if nums[mid] > target:
                r = mid - 1

            # If the middle element is less than target, search right half
            elif nums[mid] < target:
                l = mid + 1

            # If target is found, return the index
            elif nums[mid] == target:
                return mid

        # Target not found in the array
        return -1
```

### Time & Space Complexity
- **Time Complexity:** `O(log n)`  
- **Space Complexity:** `O(1)`

---

## 2. 🏟️ Stadium Attendance (SQL)

### Problem:
Return the records for stadiums that have at least **3 consecutive** days with `people >= 100`.

### SQL Solution:

```sql
with cte as (
    select *, 
           row_number() over(order by id asc) as rn
    from Stadium
    where people >= 100
),
cte2 as (
    select id, visit_date, people, (id - rn) as grp
    from cte
),
cte3 as (
    select grp
    from cte2
    group by grp
    having count(*) >= 3
)
select id, visit_date, people
from cte2 
where grp in (select grp from cte3)
order by visit_date asc
```

### Explanation: ISLAND AND GAP PROBLEM
- Use row difference `(id - row_number)` to group consecutive entries.
- Groups with 3 or more entries are selected.
- Final result gives all entries of qualifying groups.

---

## 3. 🧑‍💻 First Login per Player (SQL)

### Problem:
Write a query to get the first login `event_date` for each `player_id`.

### SQL Solution:

```sql
select player_id, min(event_date) as first_login
from activity 
group by player_id
```

### Explanation:
- Uses `MIN()` to get the earliest `event_date` grouped by `player_id`.

---

## 📅 Challenge Progress

- **Day:** 28 / 100  
- **Topic:** Binary Search (Python), Window Functions (SQL)  
- **Status:** ✅ Completed
