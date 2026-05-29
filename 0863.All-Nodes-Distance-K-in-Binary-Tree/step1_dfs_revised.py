# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        node_to_parent = {}

        def find_parents(node, parent):
            if node:
                node_to_parent[node] = parent
                find_parents(node.left, node)
                find_parents(node.right, node)

        find_parents(root, None)

        result = []
        seen = set()

        def traverse(node, distance):
            if not node or node in seen:
                return
            seen.add(node)

            if distance == k:
                result.append(node.val)
                return

            traverse(node.left, distance + 1)
            traverse(node.right, distance + 1)
            traverse(node_to_parent[node], distance + 1)

        traverse(target, 0)
        return result
