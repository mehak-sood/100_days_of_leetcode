# 100 Days of LeetCode - Day 03

## 1. Valid Anagram (Python)

### Problem Description
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

## Solutions

### Solution 1: Sorting

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same sorted characters
        return sorted(s) == sorted(t)
```

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(1)` (ignoring sorting storage, or `O(n)` if counting sorting memory)


### Solution 2: Frequency Count in One Dictionary

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict = {}

        # If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        # Count frequency of each character in string s
        for i in s:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        
        # Subtract frequency for each character in string t
        for j in t:
            if j in freq_dict:
                freq_dict[j] -= 1
            else:
                return False  # Character in t not found in s
        
        # If any frequency is not zero, they're not anagrams
        for value in freq_dict.values():
            if value != 0:
                return False
        return True
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)` (bounded by 26 English letters)


### Solution 3: Two Frequency Dictionaries

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick check on length
        if len(s) != len(t):
            return False

        s_freq_dict = {}
        t_freq_dict = {}

        # Build frequency dictionaries for both strings
        for i in range(len(s)):
            s_freq_dict[s[i]] = s_freq_dict.get(s[i], 0) + 1
            t_freq_dict[t[i]] = t_freq_dict.get(t[i], 0) + 1
        
        # Compare the dictionaries
        return s_freq_dict == t_freq_dict
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)` (bounded by number of unique characters)

### Explanation
1. The soltion 1 sorts both strings and comparing checks character order and count simultaneously.
2. The solution 2 uses a frequency dictionary allows linear-time counting and comparison of characters.
3. The Solution 3 uses two separate dictionaries track counts independently and then compare the resulting mappings.


## 2. Product Filter & Referee Query (SQL)

### Problem 1: Filter products that are low fat and recyclable

```sql
-- Select product IDs where the product is both low fat and recyclable
select product_id
from products 
where low_fats = 'Y'
and recyclable = 'Y'
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`  

### Explanation
1. **Product Filter Query**:  
   This query selects all `product_id`s from the `products` table where both conditions are met: the product is low fat (`low_fats = 'Y'`) and recyclable (`recyclable = 'Y'`). The `AND` clause ensures both criteria are satisfied simultaneously.


### Problem 2: Retrieve customer names who do not have referee_id = 2

```sql
-- Select names of customers who do not have referee_id = 2, or have no referee
select name 
from customer 
where referee_id <> 2
or referee_id is null
```

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`  

### Explanation
1. **Customer Referee Query**:  
   This query selects the `name` of customers whose `referee_id` is **not equal to 2**, or who **don’t have a referee** (i.e., `referee_id IS NULL`). The `OR` condition allows inclusion of both scenarios: not referred by 2, and no referee at all.


## Challenge Progress

- **Day:** 03 / 100  
- **Topic:** Strings/Arrays in Python & Filtering in SQL  
- **Status:** ✅ Completed