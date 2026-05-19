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

        def traverse_and_store_rightmost(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            if depth < len(result):
                result[depth] = node.val
            else:
                result.append(node.val)
            traverse_and_store_rightmost(node.left, depth + 1)
            traverse_and_store_rightmost(node.right, depth + 1)

        traverse_and_store_rightmost(root, 0)
        return result
