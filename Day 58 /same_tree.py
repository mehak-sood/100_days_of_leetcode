# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: If both nodes are null, trees are identical at this point
        if not p and not q:
            return True

        # If only one of the nodes is null, trees differ
        if not p or not q:
            return False

        # If current node values differ, trees differ
        if p.val != q.val:
            return False

        # Recursively compare left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
