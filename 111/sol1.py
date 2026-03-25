from collections import deque


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
        frontier = deque()
        frontier.append((1, root))
        while frontier:
            depth, node = frontier.popleft()
            if node.right is None and node.left is None:
                return depth
            for child in (node.left, node.right):
                if child is None:
                    continue
                frontier.append((depth + 1, child))
        raise RuntimeError("unreachable")
