# 100 Days of LeetCode - Day 14

## 1. Trapping Rain Water (Python)

### Problem Description
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### ✅ Solution 1: Brute Force (O(n²) Time)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0  # Total water trapped
        for i in range(1, len(height)-1):  # Ignore first and last bar
            l_max, r_max = 0, 0

            # Find max to the left
            for j in range(i, -1, -1):
                l_max = max(l_max, height[j])

            # Find max to the right
            for j in range(i, len(height)):
                r_max = max(r_max, height[j])

            # Add water that can be trapped at position i
            res += min(l_max, r_max) - height[i]
        
        return res
```

---

### ✅ Solution 2: Prefix Arrays (O(n) Time, O(n) Space)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        res = 0
        n = len(height)
        l_max = [0] * n
        r_max = [0] * n

        # Fill left max
        l_max[0] = height[0]
        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], height[i])

        # Fill right max
        r_max[n - 1] = height[n - 1]
        for j in range(n - 2, -1, -1):
            r_max[j] = max(r_max[j + 1], height[j])

        # Compute water
        for i in range(1, n - 1):
            res += min(l_max[i], r_max[i]) - height[i]

        return res
```

---

### ✅ Solution 3: Two Pointers (O(n) Time, O(1) Space)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        res = 0
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0

        while l < r:
            if height[l] < height[r]:
                l_max = max(l_max, height[l])
                res += l_max - height[l]
                l += 1
            else:
                r_max = max(r_max, height[r])
                res += r_max - height[r]
                r -= 1

        return res
```

---

## 2. Player Retention (SQL)

### Problem Description
Report the fraction of players who logged in again on the day after their first login.

### ✅ SQL Solution

```sql
with first_login as (
    select player_id, min(event_date) as first_login
    from activity 
    group by player_id
)

select ifnull(
    round(
        count(distinct f.player_id) / count(distinct a.player_id), 2
    ), 
0) as fraction
from activity a 
left join first_login f
    on a.player_id = f.player_id
    and datediff(a.event_date, f.first_login) = 1
```

---

## 3. Exam Attendance (SQL)

### Problem Description
Report the number of times each student attended each exam subject.

### ✅ SQL Solution

```sql
with cte as (
    select s.student_id, s.student_name, subject_name
    from students s, subjects
)

select 
    s.student_id, 
    s.student_name, 
    s.subject_name, 
    count(e.subject_name) as attended_exams
from cte s 
left join examinations e
    on s.student_id = e.student_id
    and s.subject_name = e.subject_name
group by 1, 2, 3
order by 1, 3;
```

---

## Challenge Progress

- **Day:** 14 / 100  
- **Topic:** Rain Water Trapping + SQL Joins  
- **Status:** ✅ Completed
