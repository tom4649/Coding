# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_leaf(self, node):
        if node is None:
            return False
        return node.left is None and node.right is None

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        diff = targetSum - root.val
        if self.is_leaf(root):
            return diff == 0
        return self.hasPathSum(root.left, diff) or self.hasPathSum(root.right, diff)
