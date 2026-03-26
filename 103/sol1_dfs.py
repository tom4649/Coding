from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels: List[List[int]] = []

        def traverse(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return

            while len(levels) <= depth:
                levels.append([])

            if depth % 2 == 0:
                levels[depth].append(node.val)
            else:
                levels[depth].insert(0, node.val)

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)
        return levels
