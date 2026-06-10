"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        node_copy = Node(val=node.val)
        frontier = [(node, node_copy)]
        original_to_copy = {node: node_copy}

        while frontier:
            node_original, node_copy = frontier.pop()
            for child in node_original.neighbors:
                if child in original_to_copy:
                    child_copy = original_to_copy[child]
                else:
                    child_copy = Node(val=child.val)
                    original_to_copy[child] = child_copy
                    frontier.append((child, child_copy))
                node_copy.neighbors.append(child_copy)

        return original_to_copy[node]
