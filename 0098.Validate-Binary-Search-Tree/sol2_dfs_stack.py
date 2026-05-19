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

        frontier = [(root, -float("inf"), float("inf"))]
        while frontier:
            node, must_be_greater_than, must_be_less_than = frontier.pop()
            if not must_be_greater_than < node.val < must_be_less_than:
                return False
            if node.left is not None:
                frontier.append((node.left, must_be_greater_than, node.val))
            if node.right is not None:
                frontier.append((node.right, node.val, must_be_less_than))

        return True
