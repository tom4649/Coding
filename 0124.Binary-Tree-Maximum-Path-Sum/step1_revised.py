import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = -math.inf

        def update_max_sum(node):
            # update the max sum of the tree
            # return the max sum using the node as the root of the path
            nonlocal max_sum
            if node is None:
                return -math.inf
            max_sum_left = update_max_sum(node.left)
            max_sum_right = update_max_sum(node.right)
            max_sum_self = node.val + max(0, max_sum_left, max_sum_right)
            max_sum = max(max_sum, max_sum_self, node.val + max_sum_left + max_sum_right)
            return max_sum_self

        update_max_sum(root)
        return max_sum
