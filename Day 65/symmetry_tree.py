# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # A tree is symmetric if it's a mirror of itself
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        # If both nodes are None, it's symmetric at this level
        if t1 is None and t2 is None:
            return True
        # If only one of the nodes is None, it's asymmetric
        if t1 is None or t2 is None:
            return False
        # Recursively check:
        # 1. The current node values are equal
        # 2. The left subtree of t1 is a mirror of the right subtree of t2
        # 3. The right subtree of t1 is a mirror of the left subtree of t2
        return (
            t1.val == t2.val
            and self.isMirror(t1.right, t2.left)
            and self.isMirror(t1.left, t2.right)
        )
