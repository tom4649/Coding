import copy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def merge_trees_helper(node1, node2):
            if node1 is None:
                return node2
            if node2 is None:
                return node1
            node1.val += node2.val
            node1.left = merge_trees_helper(node1.left, node2.left)
            node1.right = merge_trees_helper(node1.right, node2.right)
            return node1

        root1_copy = copy.deepcopy(root1)
        root2_copy = copy.deepcopy(root2)
        return merge_trees_helper(root1_copy, root2_copy)
