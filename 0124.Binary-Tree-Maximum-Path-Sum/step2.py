import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        def get_max_sums(node):
            # 返り値: (部分木の最大パス和, 親へ繋げられる片側の枝の最大和)
            if node is None:
                return -math.inf, 0

            left_max_sum, left_branch_max = get_max_sums(node.left)
            right_max_sum, right_branch_max = get_max_sums(node.right)

            subtree_max = max(left_max_sum, right_max_sum, node.val + left_branch_max + right_branch_max)
            branch_max = max(0, node.val + max(left_branch_max, right_branch_max))

            return subtree_max, branch_max

        max_sum, _ = get_max_sums(root)
        return max_sum
