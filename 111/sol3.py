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
        min_depth = float("inf")

        def traverse(node, depth):
            nonlocal min_depth
            if node.left is None and node.right is None:
                min_depth = min(min_depth, depth)
                return
            for child in (node.left, node.right):
                if child is None:
                    continue
                traverse(child, depth + 1)

        traverse(root, 1)
        return min_depth
