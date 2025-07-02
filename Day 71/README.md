# 100 Days of LeetCode - Day 71

## 1. Merge Alternately (Python)

### Problem Description

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If one string is longer than the other, append the additional letters at the end.

### Python Solution

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)  # Length of first string
        n = len(word2)  # Length of second string
        res = []  # List to store the merged characters
        i = 0
        j = 0

        # Continue until we've exhausted both strings
        while i < m or j < n:
            if i < m:
                res += word1[i]  # Append character from word1 if not exhausted
                i += 1
            if j < n:
                res += word2[j]  # Append character from word2 if not exhausted
                j += 1

        return "".join(res)  # Join the list into a single string
```

**Time Complexity:** `O(m + n)`
**Space Complexity:** `O(m + n)`

### Explanation

The solution uses two pointers to iterate through both strings and adds characters in alternating order. Remaining characters from the longer string are appended at the end.

---

## 2. Cheapest Flight with 0, 1 or 2 Stops (SQL)

### Problem Description

Find the minimum cost between all origin-destination pairs in a flight table, where a flight can have 0, 1, or 2 stops.

### SQL Solution

```sql
-- One-stop connections
with one_stop as (
    select distinct o.origin, s1.destination, (o.cost + s1.cost) as trip_cost
    from da_flights o
    join da_flights s1 on o.destination = s1.origin
),

-- Two-stop connections
two_stops as (
    select distinct
        o.origin,
        o.destination as stop1,
        s1.destination as stop2,
        s2.destination as destination,
        (o.cost + s1.cost + s2.cost) as trip_cost
    from da_flights o
    join da_flights s1 on o.destination = s1.origin
    join da_flights s2 on s1.destination = s2.origin
),

-- Combine all flights: direct, one-stop, two-stops
all_flights as (
    (select origin, destination, cost as trip_cost from da_flights)
    union
    (select * from one_stop)
    union
    (select origin, destination, trip_cost from two_stops)
)

-- Final result: minimum cost for each origin-destination pair
select origin, destination, min(trip_cost) as cheapest_flight
from all_flights
group by 1, 2;
```

**Time Complexity:** Depends on data size, uses joins and aggregations
**Space Complexity:** O(n) for temporary CTE tables

### Explanation

The solution builds connections with 0, 1, and 2 stops and unifies them with a `UNION`. Then, it finds the cheapest cost per origin-destination pair using `GROUP BY` and `MIN`.

---

## Challenge Progress

* **Day:** 71 / 100
* **Topic:** String Manipulation & SQL Joins
* **Status:** ✅ Completed
