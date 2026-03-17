from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional["TreeNode"]) -> List[List[int]]:
        level_order = []
        if root is None:
            return level_order
        children_pushed = deque([(0, root)])

        while children_pushed:
            level, node = children_pushed.pop()
            for child in (node.right, node.left):
                if child is not None:
                    children_pushed.append((level + 1, child))
            while len(level_order) <= level:
                level_order.append([])
            level_order[level].append(node.val)
        return level_order
