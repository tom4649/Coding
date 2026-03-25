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

        def push_it_and_left_children(node):
            while node is not None:
                frontier.append(node)
                node = node.left

        push_it_and_left_children(root)
        min_value = -float("inf")
        while frontier:
            node = frontier.pop()
            if min_value >= node.val:
                return False
            min_value = node.val
            push_it_and_left_children(node.right)
        return True
