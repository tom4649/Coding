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
        path_to_p = []
        path_to_q = []

        def dfs(node: TreeNode | None, path: list[TreeNode]):
            if node is None or (path_to_p and path_to_q):
                return

            path.append(node)

            if node == p:
                path_to_p.extend(path)
            if node == q:
                path_to_q.extend(path)

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        dfs(root, [])

        node = root
        for node_p, node_q in zip(path_to_p, path_to_q):
            if node_p == node_q:
                node = node_p
            else:
                break

        return node
