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
        left_level_order = self.levelOrder(root.left)
        right_level_order = self.levelOrder(root.right)
        if len(left_level_order) < len(right_level_order):
            left_level_order.extend(
                [[] for _ in range(len(right_level_order) - len(left_level_order))]
            )
        else:
            right_level_order.extend(
                [[] for _ in range(len(left_level_order) - len(right_level_order))]
            )
        merged_level_order = [[root.val]]
        for i in range(len(left_level_order)):
            merged_level_order.append(left_level_order[i] + right_level_order[i])
        return merged_level_order
