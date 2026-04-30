from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        frontier = []

        def push_it_and_left(node):
            while node:
                frontier.append(node)
                node = node.left

        push_it_and_left(root)
        lower_bound_exclusive = -float("inf")

        while frontier:
            node = frontier.pop()
            if node.val <= lower_bound_exclusive:
                return False
            lower_bound_exclusive = node.val
            if node.right:
                push_it_and_left(node.right)

        return True
