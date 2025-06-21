# 100 Days of LeetCode - Day 62

## 1. Add Binary (Python)

### Problem Description

Given two binary strings `a` and `b`, return their sum as a binary string.

---

### ✅ Solution 1: Built-in Conversion

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers, add them, then convert result back to binary string
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]  # Remove '0b' prefix
```

**Time Complexity:** `O(n + m)`  
**Space Complexity:** `O(1)`

---

### ✅ Solution 2: Bitwise Logic (XOR & AND)

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)  # Convert binary to integers

        while y:
            answer = x ^ y          # XOR: adds bits without carry
            carry = (x & y) << 1    # AND + left shift = carry calculation
            x, y = answer, carry    # Continue until no carry remains

        return bin(x)[2:]  # Convert final result to binary, remove '0b'
```

**Time Complexity:** `O(1)` (bounded by bit size of input)  
**Space Complexity:** `O(1)`


**Explanation:**
- In Approach 1, we convert both binary strings to integers using int(a, 2), add them, and then convert the result back to binary using bin(), trimming the '0b' prefix. This method leverages Python’s built-in functions for a clean and simple solution.

- In Approach 2, we simulate binary addition using bitwise XOR (to add without carry) and AND + left shift (to compute the carry). We repeat this process until no carry remains. This approach mirrors how binary addition works at the hardware level and doesn’t use the + operator.
---

## 2. Most Frequent Oscar-Winning Nominee's Genre (SQL)

### Problem Description

Find the genre(s) of the nominee(s) who won the most Oscars.

---

### ✅ SQL Solution

```sql
-- Step 1: Count wins per nominee and rank them
with cte as (
    select nominee, count(*) as wins, 
           dense_rank() over(order by count(*) desc) as rnk
    from oscar_nominees
    where winner = 1
    group by 1
),

-- Step 2: Get top-ranked (most-winning) nominee(s)
cte2 as (
    select nominee 
    from cte
    where rnk = 1
)

-- Step 3: Return genres of these nominees
select distinct top_genre
from nominee_information a
join cte2 b
on a.name = b.nominee;
```

**Explanation:**
- `cte`: Ranks nominees by number of wins.
- `cte2`: Extracts top winner(s).
- Final query: Joins nominee info to fetch distinct genres.

---

## 📅 Challenge Progress

- **Day:** 62 / 100  
- **Topic:** Binary Math & SQL Aggregation  
- **Status:** ✅ Completed
