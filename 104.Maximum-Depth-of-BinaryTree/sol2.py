# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if node is None:
                return depth
            depth_l = depth_r = 0
            if node.left is not None:
                depth_l = dfs(node.left, depth + 1)
            if node.right is not None:
                depth_r = dfs(node.right, depth + 1)
            return max([depth, depth_l, depth_r])

        dummy = TreeNode(-float("inf"), right=root)
        return dfs(dummy, 0)
