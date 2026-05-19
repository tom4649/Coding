from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        result: list[int] = []
        frontier = [root]

        while frontier:
            result.append(frontier[-1].val)

            next_frontier: list[TreeNode] = []
            for node in frontier:
                if node.left is not None:
                    next_frontier.append(node.left)
                if node.right is not None:
                    next_frontier.append(node.right)
            frontier = next_frontier

        return result
