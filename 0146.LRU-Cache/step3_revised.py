class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.key_to_node = {}
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def _insert_front(self, node: Node) -> None:
        node.next = self.sentinel.next
        node.prev = self.sentinel
        self.sentinel.next.prev = node
        self.sentinel.next = node

    def _delete(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._delete(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._delete(node)
            self._insert_front(node)
            return
        node = Node(key=key, val=value)
        self._insert_front(node)
        self.key_to_node[key] = node
        if len(self.key_to_node) > self.capacity:
            lru = self.sentinel.prev
            self._delete(lru)
            del self.key_to_node[lru.key]
