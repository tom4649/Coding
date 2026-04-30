from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        frontier = [(root, -float("inf"), float("inf"))]

        while frontier:
            node, lower_bound_exclusive, upper_bound_exclusive = frontier.pop()
            if not node:
                continue
            if not lower_bound_exclusive < node.val < upper_bound_exclusive:
                return False
            frontier.append((node.left, lower_bound_exclusive, node.val))
            frontier.append((node.right, node.val, upper_bound_exclusive))
        return True
