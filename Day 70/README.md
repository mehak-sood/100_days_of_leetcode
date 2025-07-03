# 100 Days of LeetCode - Day 70

## 1. Roman to Integer (Python)

### Problem Description

Given a Roman numeral string `s`, convert it to an integer.

### Solution 1: Right-to-Left Traversal with Previous Comparison

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 'I'
        res = 0
        for i in range(len(s)-1, -1, -1):  # Traverse from right to left
            char = s[i]
            if dict[char] < dict[prev]:
                res -= dict[char]  # Subtract if smaller than previous
            else:
                res += dict[char]  # Else, add normally
            prev = char
        return res
```

### Solution 2: Left-to-Right Traversal with Lookahead

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        result = 0
        for i in range(0, len(s)-1):
            j = i + 1
            if my_dict[s[j]] > my_dict[s[i]]:
                result -= my_dict[s[i]]  # Subtract if next is greater
            else:
                result += my_dict[s[i]]
        return result + my_dict[s[-1]]  # Always add the last numeral
```

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Explanation:

* Roman numerals subtract smaller values when placed before larger values (e.g., IV = 5 - 1).
* The first approach uses right-to-left comparison with a `prev` tracker.
* The second approach uses left-to-right traversal with a lookahead strategy.

---

## 2. Most Active Client for High Call Users (SQL)

### Problem Description

Find the client that generated the most events for users who made/received calls in at least 50% of their events.

### SQL Query

```sql
WITH cte AS (
  SELECT user_id,
         SUM(CASE
                 WHEN event_type IN ('video call received', 'video call sent', 'voice call received', 'voice call sent')
                 THEN 1 ELSE 0 END) / COUNT(*) * 100 AS perc
  FROM fact_events
  GROUP BY 1
  HAVING perc >= 50
)

SELECT client_id
FROM (
  SELECT client_id,
         DENSE_RANK() OVER(ORDER BY COUNT(*) DESC) AS rnk
  FROM fact_events
  WHERE user_id IN (SELECT user_id FROM cte)
  GROUP BY 1
) a
WHERE rnk = 1
```

### Explanation:

* Identify users with ≥50% call-related events using a `CASE` condition and aggregate.
* From these users, find the client(s) who have the most events using `DENSE_RANK()`.
* Return the top-ranked client(s).

**Time Complexity:** O(n)
**Space Complexity:** O(1) (ignoring result size)

---

## Challenge Progress

* **Day:** 70 / 100
* **Topic:** Roman Numerals, Event Aggregation
* **Status:** ✅ Completed
