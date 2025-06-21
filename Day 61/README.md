# 100 Days of LeetCode - Day 61

## 1. Implement strStr() (Python)

### Problem Description

Implement `strStr()`. Return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

---

### ✅ Solution 1: Built-in Method

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Use Python's built-in string method find()
        # Returns -1 if needle not found
        return haystack.find(needle)
```

**Time Complexity:** `O(n * m)` (worst case, though optimized internally)  
**Space Complexity:** `O(1)`

---

### ✅ Solution 2: Manual Window Search

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        # Slide a window of size m over haystack
        for win in range(0, n - m + 1):
            for i in range(m):
                if needle[i] != haystack[win + i]:  # Mismatch found
                    break
                if i == m - 1:  # Reached end of needle and all matched
                    return win
        return -1  # No match found
```

**Time Complexity:** `O(n * m)`  
**Space Complexity:** `O(1)`

---

## 2. Actor Rating Difference (SQL)

### Problem Description

Return each actor's average rating (excluding the latest film) and latest film rating. If the actor has only one movie, compare it with itself.

---

### ✅ SQL Solution

```sql
-- Get latest film release date per actor
with cte as (
    select actor_name, max(release_date) as latest_film_release
    from actor_rating_shift
    group by 1
),

-- Find actors with only one film
t1 as (
    select actor_name
    from actor_rating_shift
    group by 1
    having count(*) = 1 
),

-- Compute average rating excluding latest film, unless only one film
cte2 as (
    select actor_name, avg(film_rating) as avg_rating
    from actor_rating_shift
    where (actor_name, release_date) not in (select * from cte)
       or actor_name in (select * from t1)
    group by 1
),

-- Get latest film rating per actor
cte3 as (
    select a.actor_name, film_rating as latest_rating 
    from actor_rating_shift a
    join cte b
    on a.actor_name = b.actor_name
    and a.release_date = b.latest_film_release
)

-- Final output: actor name, average rating, latest rating, and difference
select a.actor_name, avg_rating, latest_rating, 
       (latest_rating - avg_rating) as rating_difference
from cte2 a
join cte3 b
on a.actor_name = b.actor_name
```

---

## 📅 Challenge Progress

- **Day:** 61 / 100  
- **Topic:** String Matching & Complex SQL Aggregates  
- **Status:** ✅ Completed
