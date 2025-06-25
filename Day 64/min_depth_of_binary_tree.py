### Solution 1: DFS (Depth First Search)

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




### Solution 2: BFS (Breadth First Search)

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