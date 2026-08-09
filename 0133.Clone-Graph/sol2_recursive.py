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

        original_to_copy = {}

        def traverse(node):
            if node in original_to_copy:
                return original_to_copy[node]
            node_copy = Node(val=node.val)
            original_to_copy[node] = node_copy
            for child in node.neighbors:
                traverse(child)
                node_copy.neighbors.append(original_to_copy[child])

        traverse(node)
        return original_to_copy[node]
