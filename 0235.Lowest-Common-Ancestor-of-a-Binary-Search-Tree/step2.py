# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        smaller, larger = sorted((p.val, q.val))
        node = root
        while True:
            if smaller <= node.val <= larger:
                return node
            if node.val < smaller:
                node = node.right
                continue
            if node.val > larger:
                node = node.left
        return None
