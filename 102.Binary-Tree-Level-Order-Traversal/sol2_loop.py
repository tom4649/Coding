from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional["TreeNode"]) -> List[List[int]]:
        if root is None:
            return []
        level_order = []
        node_to_traverse = deque([(0, root)])

        while node_to_traverse:
            level, node = node_to_traverse.pop()
            for child in (node.right, node.left):
                if child is not None:
                    node_to_traverse.append((level + 1, child))
            while len(level_order) <= level:
                level_order.append([])
            level_order[level].append(node.val)
        return level_order
