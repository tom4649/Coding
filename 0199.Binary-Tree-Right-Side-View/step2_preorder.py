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

        result = []

        def traverse(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return

            if len(result) == depth:
                result.append(node.val)

            traverse(node.right, depth + 1)
            traverse(node.left, depth + 1)

        traverse(root, 0)
        return result
