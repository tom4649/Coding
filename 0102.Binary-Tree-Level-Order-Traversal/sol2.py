# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional["TreeNode"]) -> List[List[int]]:
        level_order = []

        def append_value_by_level(node, level):
            if node is None:
                return

            if level == len(level_order):
                level_order.append([])
            level_order[level].append(node.val)

            append_value_by_level(node.left, level + 1)
            append_value_by_level(node.right, level + 1)

        append_value_by_level(root, 0)
        return level_order
