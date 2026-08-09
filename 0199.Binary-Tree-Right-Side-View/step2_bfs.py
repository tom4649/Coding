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
        depth = 0

        while frontier:
            next_frontier: list[Optional[TreeNode]] = []

            for node in frontier:
                if node is None:
                    continue
                if len(result) == depth:
                    result.append(node.val)
                next_frontier.append(node.right)
                next_frontier.append(node.left)

            frontier = next_frontier
            depth += 1

        return result
