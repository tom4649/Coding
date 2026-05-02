from collections import deque


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
        node_to_depth = {}
        frontier = deque()
        frontier.append((root, False))
        while frontier:
            node, is_visited = frontier.pop()
            if node is None:
                continue
            if not is_visited:
                frontier.append((node, True))
                frontier.append((node.left, False))
                frontier.append((node.right, False))
                continue
            depth_l = node_to_depth.get(node.left, None)
            depth_r = node_to_depth.get(node.right, None)
            if depth_l is None and depth_r is None:
                node_to_depth[node] = 1
            elif depth_l is None:
                node_to_depth[node] = depth_r + 1
            elif depth_r is None:
                node_to_depth[node] = depth_l + 1
            else:
                node_to_depth[node] = min(depth_l, depth_r) + 1
        return node_to_depth[root]
