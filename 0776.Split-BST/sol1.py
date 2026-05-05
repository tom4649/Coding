from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given tree
    @param v: the target value
    @return: the root TreeNode after splitting
    """

    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:
        # write your code here
        def split_bst_helper(node):
            if node is None:
                return None, None
            if node.val > v:
                left_less_or_equal, left_greater = split_bst_helper(node.left)
                node.left = left_greater
                return left_less_or_equal, node
            else:
                right_less_or_equal, right_greater = split_bst_helper(node.right)
                node.right = right_less_or_equal
                return node, right_greater

        def size_of(node):
            if node is None:
                return 0
            return size_of(node.left) + size_of(node.right) + 1

        less_or_equal, greater = split_bst_helper(root)
        if size_of(less_or_equal) > size_of(greater):
            return less_or_equal
        return greater
