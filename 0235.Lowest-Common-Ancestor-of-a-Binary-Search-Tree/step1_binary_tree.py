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
        node_to_depth_and_parent: dict[TreeNode, tuple(int, TreeNode | None)] = {}

        depth = 1
        frontier = [(root, None)]
        found_p = False
        found_q = False
        while frontier:
            next_frontier = []
            for node, parent in frontier:
                if node is None:
                    continue
                node_to_depth_and_parent[node] = (depth, parent)
                if node == p:
                    found_p = True
                if node == q:
                    found_q = True
                if found_p and found_q:
                    break
                next_frontier.append((node.left, node))
                next_frontier.append((node.right, node))
            depth += 1
            frontier = next_frontier

        depth_p, parent_p = node_to_depth_and_parent[p]
        depth_q, parent_q = node_to_depth_and_parent[q]
        if depth_p < depth_q:
            depth_p, depth_q = depth_q, depth_p
            parent_p, parent_q = parent_q, parent_p
            p, q = q, p
        while depth_p > depth_q:
            p = parent_p
            depth_p, parent_p = node_to_depth_and_parent[p]
        while p != q:
            p = parent_p
            depth_p, parent_p = node_to_depth_and_parent[p]
            q = parent_q
            depth_q, parent_q = node_to_depth_and_parent[q]

        return p
