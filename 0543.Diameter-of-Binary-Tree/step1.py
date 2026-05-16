from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        diameter = 0

        def depth_of(node):
            nonlocal diameter
            if node is None:
                return 0

            depth_left = depth_of(node.left)
            depth_right = depth_of(node.right)
            diameter = max(diameter, depth_left + depth_right)

            return max(depth_left, depth_right) + 1

        depth_of(root)
        return diameter
