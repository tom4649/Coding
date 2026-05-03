import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level_order = []

        level_nodes = collections.deque([root])

        while True:
            next_level_nodes = []
            values_by_level = []
            while level_nodes:
                node = level_nodes.popleft()
                values_by_level.append(node.val)
                for child in (node.left, node.right):
                    if child is not None:
                        next_level_nodes.append(child)
            level_order.append(values_by_level)
            if not next_level_nodes:
                return level_order
            level_nodes = collections.deque(next_level_nodes)

        raise RuntimeError("unreachable")
