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
        stack = [(root, False)]

        while stack:
            node, seen_left = stack.pop()
            if node is None:
                continue
            if seen_left:
                num_seen += 1
                if num_seen == k:
                    return node.val
                stack.append((node.right, False))
                continue
            stack.append((node, True))
            stack.append((node.left, False))

        return None
