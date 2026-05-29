import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        if k == 0:
            return [target.val]

        graph = collections.defaultdict(list)

        def create_graph(node, parent):
            for child in (node.left, node.right):
                if child is not None:
                    graph[node].append(child)
                    create_graph(child, node)
            if parent is not None:
                graph[node].append(parent)

        create_graph(root, None)

        seen = {target}
        frontier = [target]
        distance = 0
        while frontier:
            next_frontier = []
            for node in frontier:
                seen.add(node)
                for child in graph[node]:
                    if child is not None and child not in seen:
                        next_frontier.append(child)
            frontier = next_frontier
            distance += 1
            if distance == k:
                break
        return [node.val for node in frontier]
