# 100 Days of LeetCode - Day 58

## 1. Same Tree (Python)

### Problem Description

Given two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### Solution: Recursive Comparison

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, they are the same at this position
        if not p and not q:
            return True
        # If only one of the nodes is null, the trees are different
        if not p or not q:
            return False
        # If current node values are different, return False
        if p.val != q.val:
            return False
        # Recursively compare left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

**Time Complexity:** `O(n)` – Visit every node once
**Space Complexity:** `O(h)` – Recursion stack, where h is the height of the tree

---

## 2. SQL – Count of Flags Reviewed by YouTube for Most Flagged Video

### Problem Description

Find the number of user flags that were reviewed by YouTube for the video(s) that received the most user flags.

### SQL Solution

```sql
-- Step 1: Rank videos by the number of flags
with cte as (
    select video_id,
           dense_rank() over(order by count(flag_id) desc) as rnk
    from user_flags
    group by video_id
)

-- Step 2: Count reviewed flags for the top-ranked video(s)
select video_id,
       count(b.flag_id) as yt_reviewed
from (
    select *
    from user_flags
    where video_id in (
        select video_id
        from cte
        where rnk = 1  -- most-flagged video(s)
    )
) a
left join (
    select flag_id
    from flag_review
    where reviewed_by_yt = 1  -- flags reviewed by YouTube
) b
on a.flag_id = b.flag_id
group by video_id;
```

**Explanation:**

1. The CTE ranks videos by number of flags.
2. The subquery selects only the most-flagged video(s).
3. The outer query joins with the reviewed flags and counts how many were reviewed.

**Time Complexity:** `O(n log n)` (due to aggregation and ranking)
**Space Complexity:** `O(n)` (for intermediate tables and joins)

---

## Challenge Progress

* **Day:** 58 / 100
* **Topic:** Tree Recursion & SQL Joins/Filtering
* **Status:** ✅ Completed
