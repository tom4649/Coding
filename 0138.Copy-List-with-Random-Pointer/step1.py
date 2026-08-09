"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        if head is None:
            return head
        copy_head = Node(x=head.val)
        original_to_copy = {head: copy_head}
        node = head
        node_copy = copy_head
        while node is not None:
            if node.next is not None:
                if node.next in original_to_copy:
                    node_copy.next = original_to_copy[node.next]
                else:
                    node_copy.next = Node(x=node.next.val)
                    original_to_copy[node.next] = node_copy.next
            if node.random is not None:
                if node.random in original_to_copy:
                    node_copy.random = original_to_copy[node.random]
                else:
                    node_copy.random = Node(x=node.random.val)
                    original_to_copy[node.random] = node_copy.random
            node = node.next
            node_copy = node_copy.next
        return copy_head
