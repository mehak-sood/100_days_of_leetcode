# 100 Days of LeetCode - Day 65

## 1. Symmetric Tree (Python)

### Problem Description

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Solutions

### Solution: Recursive Mirror Check

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # A tree is symmetric if it is a mirror of itself
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        # Both nodes are None, so it's symmetric at this point
        if t1 is None and t2 is None:
            return True
        # Only one node is None, asymmetry found
        if t1 is None or t2 is None:
            return False
        # Check if current values match and recurse on mirrored children
        return (
            t1.val == t2.val and
            self.isMirror(t1.right, t2.left) and
            self.isMirror(t1.left, t2.right)
        )
```

**Time Complexity:** `O(n)` - where n is the number of nodes in the tree.

**Space Complexity:** `O(h)` - where h is the height of the tree (due to recursion stack).

### Explanation

This solution checks whether the left and right subtrees are mirror images of each other. It uses a helper function `isMirror` that recursively compares the left subtree of one node with the right subtree of the other.

---

## 2. Consecutive Month Trips (SQL)

### Problem Description

Find drivers who had completed trips in **two consecutive months**.

### SQL Solution

```sql
-- CTE to get distinct completed trips with driver and date
with cte as (
    select distinct driver_id, trip_date
    from uber_trips
    where is_completed = 1
)

-- Join CTE with itself to find trips in consecutive months
select distinct t1.driver_id
from cte t1
join cte t2
    on t1.driver_id = t2.driver_id
    -- Match if t2's month is exactly one month after t1's month
    and date_format(date_add(t1.trip_date, interval 1 month), '%Y%m') = date_format(t2.trip_date, '%Y%m')
```

**Time Complexity:** `O(n^2)` in worst case due to self join.

**Explanation:**

1. The query finds all distinct completed trips.
2. It then joins the table to itself to compare a driver's trips in adjacent months using `DATE_ADD()` and `DATE_FORMAT()`.
3. If such a pair exists, the driver ID is returned.

---

## Challenge Progress

* **Day:** 65 / 100
* **Topic:** Binary Trees & SQL Joins/Date Logic
* **Status:** ✅ Completed
