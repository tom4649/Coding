# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def update_max_depth(node, depth):
            nonlocal max_depth
            if node is None:
                return
            max_depth = max(max_depth, depth)
            update_max_depth(node.left, depth + 1)
            update_max_depth(node.right, depth + 1)
            return

        update_max_depth(root, 1)
        return max_depth
