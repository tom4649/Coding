import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        zigzag_level_order = []
        level_nodes = collections.deque([root])
        left_to_right = True

        while True:
            values_by_level = []
            next_nodes = []
            while level_nodes:
                node = level_nodes.popleft()
                values_by_level.append(node.val)
                for child in (node.left, node.right):
                    if child is not None:
                        next_nodes.append(child)
            if not left_to_right:
                values_by_level.reverse()
            zigzag_level_order.append(values_by_level)
            if not next_nodes:
                return zigzag_level_order
            level_nodes = collections.deque(next_nodes)
            left_to_right = not left_to_right
