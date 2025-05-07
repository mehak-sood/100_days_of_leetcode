# 100 Days of LeetCode - Day 16

## 1. Longest Substring Without Repeating Characters (Python)

### Problem Description

Given a string `s`, find the length of the longest substring without repeating characters.

## Solutions

### ✅ Solution 1: Brute Force (O(n^3) Time)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n  # For strings with 0 or 1 character, return length directly

        def check(start, end):
            # Helper function to check if all characters in s[start:end+1] are unique
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        max_len = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    max_len = max(max_len, j - i + 1)
        return max_len
```

**Time Complexity:** `O(n^3)`
**Space Complexity:** `O(min(n, m))` where `m` is the character set size

### ✅ Solution 2: Sliding Window with Set (O(n) Time)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        seen = set()
        l, r = 0, 0
        max_len = 0

        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1
        return max_len
```

**Time Complexity:** `O(n)`
**Space Complexity:** `O(min(n, m))` where `m` is the character set size

### ✅ Solution 3: Sliding Window with Hash Map (O(n) Time)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_index = {}  # Store last seen index of each character
        max_len = 0
        l, r = 0, 0

        while r < n:
            # If character is already in window, move left pointer
            if s[r] in char_index and char_index[s[r]] >= l:
                l = char_index[s[r]] + 1
            char_index[s[r]] = r  # Update last seen index
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
```

**Time Complexity:** `O(n)`
**Space Complexity:** `O(min(n, m))` where `m` is the character set size

### Explanation

1. **Brute Force**: Try all substrings, check if characters are unique.
2. **Sliding Window with Set**: Expand and contract window to maintain a set of unique characters.
3. **Sliding Window with Hash Map**: Use a dictionary to remember last seen indices and skip to avoid re-checking.

## 2. SQL Problems

### ✅ Problem 1: Duplicate Emails

```sql
SELECT DISTINCT p1.email
FROM person p1
JOIN person p2
  ON p1.email = p2.email
 AND p1.id <> p2.id
```

**Time Complexity:** `O(n^2)`
**Space Complexity:** `O(1)`

### Explanation

* This query finds emails that appear more than once by joining the table with itself on the email column but excluding rows with the same ID.

### ✅ Problem 2: Weight Limit Queue

```sql
WITH cte AS (
    SELECT person_name,
           SUM(weight) OVER(ORDER BY turn ASC) AS agg_sum
    FROM queue
)

SELECT person_name
FROM cte
WHERE agg_sum <= 1000
ORDER BY agg_sum DESC
LIMIT 1;
```

**Time Complexity:** `O(n)`
**Space Complexity:** `O(n)`

### Explanation

* This query calculates the cumulative weight of people entering in turn order.
* It returns the name of the last person that keeps the sum within the 1000 weight limit.

## Challenge Progress

* **Day:** 16 / 100
* **Topic:** Sliding Window Problem + SQL Self-Join & Window Functions
* **Status:** ✅ Completed
