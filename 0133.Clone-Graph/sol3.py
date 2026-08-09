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

        original_to_copy = {node: Node(val=node.val)}
        frontier = [node]

        while frontier:
            node_original = frontier.pop()
            for child in node_original.neighbors:
                if child not in original_to_copy:
                    original_to_copy[child] = Node(val=child.val)
                    frontier.append(child)
                original_to_copy[node_original].neighbors.append(
                    original_to_copy[child]
                )

        return original_to_copy[node]
