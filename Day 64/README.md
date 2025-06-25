# 100 Days of LeetCode - Day 64

## 1. Minimum Depth of Binary Tree (Python)

### Problem Description

Given a binary tree, find its **minimum depth**. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

### Solution 1: DFS (Depth First Search)

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if root is None:
                return 0  # Base case: empty node has depth 0

            if root.left is None:
                return 1 + dfs(root.right)  # Only right subtree exists
            elif root.right is None:
                return 1 + dfs(root.left)   # Only left subtree exists

            return 1 + min(dfs(root.left), dfs(root.right))  # Both children exist

        return dfs(root)
```

**Time Complexity:** `O(n)` — Each node is visited once.

**Space Complexity:** `O(h)` — Height of the tree (for recursion stack).

### Solution 2: BFS (Breadth First Search)

```python
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # No node means depth is 0

        queue = deque([(root, 1)])  # Each entry holds (node, current_depth)

        while queue:
            node, depth = queue.popleft()

            # If we reach a leaf node, return the current depth
            if not node.left and not node.right:
                return depth

            # Add child nodes to the queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
```

**Time Complexity:** `O(n)` — In the worst case, we may visit all nodes.

**Space Complexity:** `O(n)` — For the queue storage.

### Explanation:

* DFS explores all paths down to leaves and selects the shortest one.
* BFS returns the depth as soon as it finds the first leaf, making it efficient for minimum depth problems.

---

## 2. SQL: Count LinkedIn Users Who Switched from Microsoft to Google

### Problem Statement

Find the number of users who changed their employer from **Microsoft** to **Google**.

### SQL Solution:

```sql
-- Create a CTE to compare current and previous employer per user based on start date
with cte as (
    select 
        user_id, 
        employer, 
        lag(employer, 1) over(
            partition by user_id 
            order by start_date asc
        ) as prev_employer  -- Gets the employer immediately before current one
    from linkedin_users
)

-- Count number of users whose current employer is Google
-- and immediately previous employer was Microsoft
select count(user_id)
from cte
where employer = 'Google'
  and prev_employer = 'Microsoft';

```

### Explanation:

* Use `LAG` to find each user's previous employer.
* Filter for cases where the user moved from `Microsoft` to `Google`.
* `COUNT` the number of such users.

**Time Complexity:** `O(n log n)` (due to window function ordering)

**Space Complexity:** `O(n)`

---

## Challenge Progress

* **Day:** 64 / 100
* **Topic:** Trees (DFS/BFS) + SQL Window Functions
* **Status:** ✅ Completed
