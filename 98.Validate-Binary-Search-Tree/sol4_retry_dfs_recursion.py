from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_with_bound(node, lower_bound_exclusive, upper_bound_exclusive):
            if not node:
                return True
            if not lower_bound_exclusive < node.val < upper_bound_exclusive:
                return False
            is_valid_left = is_valid_with_bound(
                node.left, lower_bound_exclusive, node.val
            )
            is_valid_right = is_valid_with_bound(
                node.right, node.val, upper_bound_exclusive
            )
            return is_valid_left and is_valid_right

        return is_valid_with_bound(root, -float("inf"), float("inf"))
