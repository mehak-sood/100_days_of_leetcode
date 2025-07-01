# 100 Days of LeetCode - Day 72

## 1. Valid Word Abbreviation (Python)

### Problem Description

Given a non-empty string `word` and an abbreviation `abbr`, return whether the string matches the given abbreviation.

A valid abbreviation uses numbers to represent the number of characters abbreviated. Numbers must not have leading zeroes.

### Solution 1: Two Pointer Parsing Approach

```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a, w = 0, 0  # Pointers for abbreviation and word respectively

        while a < len(abbr) and w < len(word):
            # Case 1: Current characters match directly
            if abbr[a] == word[w]:
                a += 1
                w += 1
                continue

            # Case 2: Invalid abbreviation character (not digit and not matching letter)
            if not abbr[a].isdigit() and abbr[a] != word[w]:
                return False

            # Case 3: Abbreviation cannot start with '0' (e.g., "01" is invalid)
            if abbr[a] == '0':
                return False

            # Case 4: Parse number from abbreviation to determine skip count
            skip = 0
            while a < len(abbr) and abbr[a].isdigit():
                skip = skip * 10 + (ord(abbr[a]) - ord('0'))  # Convert digit char to int
                a += 1

            w += skip  # Skip the indicated number of characters in `word`

        # Valid abbreviation only if both pointers reach the end
        return a == len(abbr) and w == len(word)
```

**Time Complexity:** `O(n)` — where `n` is the length of the abbreviation.
**Space Complexity:** `O(1)` — uses constant space.

### Explanation:

* Two pointers traverse `abbr` and `word`. Characters match directly, or a number in `abbr` indicates how many characters in `word` to skip.
* Special checks are added to avoid abbreviations with leading zeros.

---

## 2. Twitch Session Analysis (SQL)

### Problem Description

Find users whose first session was a 'viewer' session and count how many 'streamer' sessions they have.

### SQL Solution:

```sql
-- CTE to find users whose first session was of type 'viewer'
with cte as (
    select user_id
    from (
        select user_id, session_type, session_id,
               row_number() over(partition by user_id order by session_start asc) as rnk
        from twitch_sessions
    ) a
    where rnk = 1 and session_type = 'viewer'
)

-- Count the number of 'streamer' sessions for those users
select cte.user_id, count(t.session_id) as n_cnt
from cte
left join twitch_sessions t
  on cte.user_id = t.user_id
  and t.session_type = 'streamer'  -- Only count streamer sessions
group by 1
order by 2 desc, 1 asc;
```

**Explanation:**

* The first CTE identifies users whose first session is of type `viewer`.
* The main query joins back to count `streamer` sessions per user.
* Result is ordered by number of streamer sessions (desc), and user\_id (asc).

**Time Complexity:** `O(n log n)` due to window functions.

---

## Challenge Progress

* **Day:** 72 / 100
* **Topic:** String Parsing, Window Functions, Joins
* **Status:** ✅ Completed
