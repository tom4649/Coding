# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if root is None:
            raise ValueError("root is None")

        target = k
        node = root

        while node is not None:
            left_size = node.left.size if node.left else 0

            if target == left_size + 1:
                return node.val
            elif target <= left_size:
                node = node.left
            else:
                target -= left_size + 1
                node = node.right

        return None
