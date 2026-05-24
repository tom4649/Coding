# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if root is None:
            raise ValueError("root is None")

        num_seen = 0
        kth_smallest = None

        def traverse(node: TreeNode) -> None:
            nonlocal kth_smallest, num_seen
            if node.left is not None:
                traverse(node.left)
            if kth_smallest is not None:
                return
            num_seen += 1
            if num_seen == k:
                kth_smallest = node.val
                return
            if node.right is not None:
                traverse(node.right)

        traverse(root)
        return kth_smallest
