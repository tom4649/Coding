from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        zigzag_level_order = []

        def traverse(node, depth: int):
            if node is None:
                return

            while len(zigzag_level_order) <= depth:
                zigzag_level_order.append([])

            if depth % 2 == 0:
                zigzag_level_order[depth].append(node.val)
            else:
                zigzag_level_order[depth].insert(0, node.val)

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)
        return zigzag_level_order
