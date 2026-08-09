# 参考: https://github.com/Mike0121/LeetCode/pull/49
#       https://github.com/t0hsumi/leetcode/pull/16


class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
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

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._delete(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self._delete(self.key_to_node[key])
            del self.key_to_node[key]
        node = Node(key=key, val=value)
        self._insert_front(node)
        self.key_to_node[key] = node
        if len(self.key_to_node) > self.capacity:
            lru = self.sentinel.prev
            self._delete(lru)
            del self.key_to_node[lru.key]


from collections import OrderedDict


class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
