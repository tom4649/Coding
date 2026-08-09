# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        node_to_parent = {root: None}
        root_of_target = {root: False}

        def find_target(node):
            root_of_target[node] = False
            if node == target:
                root_of_target[node] = True
                parent = node_to_parent[node]
                while parent is not None:
                    root_of_target[parent] = True
                    parent = node_to_parent[parent]
            for child in (node.left, node.right):
                if child is not None:
                    node_to_parent[child] = node
                    find_target(child)

        find_target(root)

        result = []

        def distance_k_of_children(node, count):
            if count == k:
                result.append(node.val)
                return

            for child in (node.left, node.right):
                if child is not None:
                    distance_k_of_children(child, count + 1)

        distance_k_of_children(target, 0)
        seen = {target}

        def distance_k_of_others(node, count):
            if node in seen or node is None:
                return
            seen.add(node)
            if count == k:
                result.append(node.val)
                return
            count_children = count + 1
            for child in (node.left, node.right):
                if child is not None:
                    distance_k_of_others(child, count + 1)
            parent = node_to_parent[node]
            if parent is not None:
                count_parent = count + 1
                distance_k_of_others(parent, count + 1)

        distance_k_of_others(node_to_parent[target], 1)

        return result
