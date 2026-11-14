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


    def enQueue(self, value: int) -> bool:
        if self.num_data >= self.k:
            return False

        node = Node(value)
        node.prev = self.root
        if self.root.next is not None:
            self.root.next.prev = node
            node.next = self.root.next
        else:
            node.next = self.root
            self.root.prev = node
        self.root.next = node
        self.num_data += 1
        return True

    def deQueue(self) -> bool:
        if self.num_data == 0:
            return False
        elif self.num_data == 1:
            self.root.prev = None
            self.root.next = None
        else:
            self.root.prev.prev.next = self.root
            self.root.prev = self.root.prev.prev
        self.num_data -= 1
        return True


    def Front(self) -> int:
        return self.root.prev.value if not self.isEmpty() else -1


    def Rear(self) -> int:
        return self.root.next.value if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.num_data == 0


    def isFull(self) -> bool:
        return self.num_data == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
