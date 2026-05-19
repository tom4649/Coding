# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def is_leaf(node):
    return node.left is None and node.right is None


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        remaining = targetSum - root.val
        if is_leaf(root):
            return remaining == 0
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(
            root.right, remaining
        )
