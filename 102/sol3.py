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
        queue = deque()
        queue.append(root)
        while queue:
            values_by_level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                values_by_level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            level_order.append(values_by_level)
        return level_order
