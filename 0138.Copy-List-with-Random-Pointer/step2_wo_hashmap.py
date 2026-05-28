class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node" | None) -> "Node" | None:
        if head is None:
            return None

        # original1->copy1->original2->copy2...
        node = head
        while node:
            node_next = node.next
            copy_node = Node(x=node.val)
            node.next = copy_node
            copy_node.next = node_next
            node = node_next

        # コピーしたノードのrandomを繋ぐ
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        # コピーを分離する
        node = head
        dummy_head = Node(0)
        copy_node = dummy_head

        while node:
            node_next = node.next.next

            copy_node_next = node.next
            copy_node.next = copy_node_next
            copy_node = copy_node_next

            node.next = node_next
            node = node_next

        return dummy_head.next
