# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        if root is None:
            return None
        if root == p or root == q:
            return root

        left_found = self.lowestCommonAncestor(root.left, p, q)
        right_found = self.lowestCommonAncestor(root.right, p, q)

        if left_found is None:
            return right_found
        if right_found is None:
            return left_found
        return root
