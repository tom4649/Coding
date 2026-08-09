from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MAX_NODES = 100


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        result = [-1] * MAX_NODES
        max_depth = 0

        def traverse_right_first(node: Optional[TreeNode], depth: int) -> None:
            nonlocal max_depth
            if node is None:
                return
            traverse_right_first(node.right, depth + 1)
            if result[depth] == -1:
                result[depth] = node.val
            max_depth = max(max_depth, depth)
            traverse_right_first(node.left, depth + 1)

        traverse_right_first(root, 0)
        return result[: max_depth + 1]
