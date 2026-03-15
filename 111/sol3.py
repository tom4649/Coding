# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = float("inf")
        if root is None:
            return 0

        def dfs(node, depth):
            nonlocal min_depth
            if node is None:
                return
            if node.left is None and node.right is None:
                min_depth = min(min_depth, depth)
                return
            for child in (node.left, node.right):
                if child is None:
                    continue
                dfs(child, depth + 1)
            return

        dfs(root, 1)
        return min_depth
