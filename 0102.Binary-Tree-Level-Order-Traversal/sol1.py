from itertools import zip_longest


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
        merged_level_order = [[root.val]]
        for left, right in zip_longest(
            left_level_order, right_level_order, fillvalue=[]
        ):
            merged_level_order.append(left + right)
        return merged_level_order
