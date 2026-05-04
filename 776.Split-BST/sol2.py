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
        def set_node(slot, node):
            if len(slot) == 1:
                slot[0] = node
            elif slot[1] == "left":
                slot[0].left = node
            else:
                slot[0].right = node

        def split_bst_helper(node, less_or_equal, greater):
            if node is None:
                return

            if node.val > v:
                set_node(greater, node)
                next_node = node.left
                node.left = None
                split_bst_helper(next_node, less_or_equal, [node, "left"])
            else:
                set_node(less_or_equal, node)
                next_node = node.right
                node.right = None
                split_bst_helper(next_node, [node, "right"], greater)

        def size_of(node):
            if node is None:
                return 0
            return size_of(node.left) + size_of(node.right) + 1

        less_or_equal = [None]
        greater = [None]
        split_bst_helper(root, less_or_equal, greater)
        if size_of(less_or_equal[0]) > size_of(greater[0]):
            return less_or_equal[0]
        return greater[0]
