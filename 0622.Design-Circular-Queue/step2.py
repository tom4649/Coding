
class Node:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.next = nxt
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.num_data = 0
        self.root = Node(0)
        self.root.next = self.root
        self.root.prev = self.root

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)

        tail = self.root.prev

        node.prev = tail
        node.next = self.root
        tail.next = node
        self.root.prev = node

        self.num_data += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        head = self.root.next

        self.root.next = head.next
        head.next.prev = self.root

        self.num_data -= 1
        return True

    def Front(self) -> int:
        return self.root.next.value if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.root.prev.value if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.num_data == 0

    def isFull(self) -> bool:
        return self.num_data == self.k
