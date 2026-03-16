from collections import deque


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
        que = deque()
        que.append((root, 0))
        while que:
            node, current_sum = que.pop()
            if node is None:
                continue
            current_sum += node.val
            if self.is_leaf(node) and current_sum == targetSum:
                return True
            for child in [node.left, node.right]:
                if child is not None:
                    que.append((child, current_sum))
        return False
