# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced_helper(node):
            if node is None:
                return True, 0

            is_balanced_left, height_left = is_balanced_helper(node.left)
            is_balanced_right, height_right = is_balanced_helper(node.right)
            is_balanced = (
                is_balanced_left
                and is_balanced_right
                and abs(height_left - height_right) <= 1
            )
            return is_balanced, max(height_left, height_right) + 1

        return is_balanced_helper(root)[0]
