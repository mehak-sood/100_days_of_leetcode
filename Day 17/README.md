# 100 Days of LeetCode - Day 17

## 1. Longest Repeating Character Replacement (Python)

### Problem Description

Given a string `s` and an integer `k`, return the length of the longest substring that can be obtained by replacing at most `k` characters so that all characters in the substring are the same.

## Solutions

### Solution 1: Brute Force with Character Count

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0  # Stores the max valid substring length

        for i in range(n):  # Start index of the substring
            count = [0] * 26  # Frequency array for characters A-Z
            max_freq = 0  # Max frequency of any character in the window

            for j in range(i, n):  # End index of the substring
                idx = ord(s[j]) - ord('A')  # Map char to index 0-25
                count[idx] += 1  # Update char frequency
                max_freq = max(max_freq, count[idx])  # Track most frequent char

                # If the number of characters to replace > k, it’s invalid
                if (j - i + 1) - max_freq <= k:
                    max_len = max(max_len, j - i + 1)  # Update max length

        return max_len  # Return the maximum valid window size found
```

**Time Complexity:** `O(n^2)`
**Space Complexity:** `O(1)` (fixed array of size 26)


### Solution 2: Optimized Sliding Window

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Dictionary to store frequency of characters in the window
        max_freq = 0  # Frequency of the most common character in the window
        l = 0  # Left pointer of the sliding window
        res = 0  # Result: longest valid window found

        for r in range(len(s)):  # Right pointer of the window
            count[s[r]] = count.get(s[r], 0) + 1  # Increment frequency of current char
            max_freq = max(max_freq, count[s[r]])  # Update max frequency

            # If more than k characters need replacement, shrink window
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1  # Remove char at left pointer from count
                l += 1  # Move left pointer to shrink the window

            res = max(res, r - l + 1)  # Update result with valid window size

        return res  # Return longest valid substring length
```

**Time Complexity:** `O(n)`
**Space Complexity:** `O(1)` (at most 26 characters in the dictionary)

### Explanation:
1. The Solution 1 uses brute-force solution checks every possible substring and computes the count of the most frequent character in the substring. It then checks whether we can replace all the remaining characters (i.e., total length - max\_freq) within `k` changes. If yes, it updates the maximum length.
2. The Solution 2 uses optimized sliding window maintains a window `[l, r]` such that replacing at most `k` characters makes all characters the same. The window only shrinks when the number of characters to replace exceeds `k`. The result is updated for each valid window.


## 2. SQL Problems

### Problem 1: Join Product and Sales Tables

```sql
-- Select product name, year, and price from sales and product tables
select product_name, year, price
from sales s
join product p
on s.product_id = p.product_id;
```

**Explanation:**

* Performs an inner join between `sales` and `product` tables using `product_id` as the join key.
* Selects `product_name`, `year`, and `price` from the joined result.


### Problem 2: Delete Duplicate Emails (Keep Only Lowest ID)

```sql
-- Delete duplicate email entries, keeping only the one with the smallest ID
delete p1.*
from person p1
join person p2
on p1.email = p2.email
and p1.id > p2.id;
```

**Explanation:**

* Self-joins the `person` table on duplicate `email` entries.
* Deletes the row from `p1` where its `id` is greater than that of `p2` (thus keeping the one with the smallest `id`).


## Challenge Progress

* **Day:** 17 / 100
* **Topic:** Sliding Window & SQL Joins / Duplicates
* **Status:** ✅ Completed