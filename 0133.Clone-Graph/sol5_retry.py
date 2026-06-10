# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None

        original_to_clone = {node: Node(node.val)}
        stack = [node]

        while stack:
            original_node = stack.pop()
            for neighbor_node in original_node.neighbors:
                if neighbor_node in original_to_clone:
                    original_to_clone[original_node].neighbors.append(
                        original_to_clone[neighbor_node]
                    )
                    continue
                original_to_clone[neighbor_node] = Node(neighbor_node.val)
                original_to_clone[original_node].neighbors.append(
                    original_to_clone[neighbor_node]
                )
                stack.append(neighbor_node)

        return original_to_clone[node]


a = Node(1)
b = Node(1)

print(a == b)
print(hash(a))
print(hash(b))
