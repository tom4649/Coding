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

        def update_attribute(node: Node, node_copy: Node, attribute: str) -> None:
            nonlocal original_to_copy
            if getattr(node, attribute) in original_to_copy:
                setattr(
                    node_copy, attribute, original_to_copy[getattr(node, attribute)]
                )
            else:
                setattr(node_copy, attribute, Node(x=getattr(node, attribute).val))
                original_to_copy[getattr(node, attribute)] = getattr(
                    node_copy, attribute
                )

        while node is not None:
            if node.next is not None:
                update_attribute(node, node_copy, "next")
            if node.random is not None:
                update_attribute(node, node_copy, "random")
            node = node.next
            node_copy = node_copy.next
        return copy_head
