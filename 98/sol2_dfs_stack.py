from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        frontiers = [(root, -float("inf"), float("inf"))]
        while frontiers:
            node, lower_bound, upper_bound = frontiers.pop()
            if not lower_bound < node.val < upper_bound:
                return False
            if node.left is not None:
                frontiers.append((node.left, lower_bound, node.val))
            if node.right is not None:
                frontiers.append((node.right, node.val, upper_bound))
        return True
