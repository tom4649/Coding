# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        min_depth = float("inf")
        for child in (root.right, root.left):
            if child is None:
                continue
            min_depth = min(min_depth, self.minDepth(child) + 1)
        return min_depth
