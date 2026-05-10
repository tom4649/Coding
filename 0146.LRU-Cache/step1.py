class DoublyLinkedList:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.root = DoublyLinkedList()
        self.tail = self.root

    def move_to_front(self, node: DoublyLinkedList) -> None:
        if node.next is not None:
            node.next.prev = node.prev
        elif node.prev is not self.root:
            self.tail = node.prev
        node.prev.next = node.next
        if self.root.next is not None:
            self.root.next.prev = node
        node.next = self.root.next
        node.prev = self.root
        self.root.next = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        self.move_to_front(self.key_to_node[key])
        return self.key_to_node[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.move_to_front(self.key_to_node[key])
            return
        self.key_to_node[key] = DoublyLinkedList(
            key=key, val=value, next=self.root.next, prev=self.root
        )
        if self.root.next is not None:
            self.root.next.prev = self.key_to_node[key]
        self.root.next = self.key_to_node[key]
        if len(self.key_to_node) == 1:
            self.tail = self.key_to_node[key]
        if len(self.key_to_node) > self.capacity and self.tail is not None:
            old_tail = self.tail
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            del self.key_to_node[old_tail.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
