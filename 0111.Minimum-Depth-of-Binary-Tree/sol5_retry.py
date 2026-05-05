# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        frontier = [(1, root)]
        while frontier:
            depth, node = frontier.pop()
            if node.left is None and node.right is None:
                return depth
            for direction in ["left", "right"]:
                child = getattr(node, direction)
                if child is not None:
                    frontier.append(depth + 1, child)
        raise RuntimeError("unreachable")
