from collections import defaultdict, deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        node_to_depth = defaultdict(int)
        visited_nodes = set()
        que = deque()
        que.append((root, False))
        while que:
            node, is_visited = que.pop()
            if node is None:
                continue
            if is_visited:
                depth_l = node_to_depth.get(node.left, 0)
                depth_r = node_to_depth.get(node.right, 0)
                if depth_l == 0 or depth_r == 0:
                    node_to_depth[node] = max(depth_l, depth_r) + 1
                else:
                    node_to_depth[node] = min(depth_l, depth_r) + 1
            else:
                que.append((node, True))
                que.append((node.left, False))
                que.append((node.right, False))
        return node_to_depth[root]
