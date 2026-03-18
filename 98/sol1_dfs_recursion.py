from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST_with_range(node, lower_bound, upper_bound):
            if node is None:
                return True
            if node.val <= lower_bound or node.val >= upper_bound:
                return False
            return isValidBST_with_range(
                node.left, lower_bound, min(upper_bound, node.val)
            ) and isValidBST_with_range(
                node.right, max(lower_bound, node.val), upper_bound
            )

        return isValidBST_with_range(root, -float("inf"), float("inf"))
