from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST_with_range(node, must_be_greater_than, must_be_less_than):
            if node is None:
                return True
            if node.val <= must_be_greater_than or node.val >= must_be_less_than:
                return False
            return isValidBST_with_range(
                node.left, must_be_greater_than, node.val
            ) and isValidBST_with_range(node.right, node.val, must_be_less_than)

        return isValidBST_with_range(root, -float("inf"), float("inf"))
