class Node:
    def __init__(self, count=0, keys=None):
        self.count = count
        self.keys = keys if keys is not None else set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.key_to_node = {}
        self.sentinel = Node(count=0)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            node = self.sentinel
        else:
            node = self.key_to_node[key]

        if node.next.count == node.count + 1:
            target_node = node.next
        else:
            target_node = Node(count=node.count + 1)
            self.add_node_after(target_node, node)

        target_node.keys.add(key)
        self.key_to_node[key] = target_node

        if node is not self.sentinel:
            node.keys.remove(key)
            if not node.keys:
                self.delete_node(node)

    def dec(self, key: str) -> None:
        if key not in self.key_to_node:
            return

        node = self.key_to_node[key]

        if node.count > 1:
            if node.prev.count == node.count - 1:
                target_node = node.prev
            else:
                target_node = Node(count=node.count - 1)
                self.add_node_after(target_node, node.prev)

            target_node.keys.add(key)
            self.key_to_node[key] = target_node
        else:
            del self.key_to_node[key]

        node.keys.remove(key)
        if not node.keys:
            self.delete_node(node)

    def getMaxKey(self) -> str:
        max_node = self.sentinel.prev
        if max_node is self.sentinel:
            return ""
        return next(iter(max_node.keys))

    def getMinKey(self) -> str:
        min_node = self.sentinel.next
        if min_node is self.sentinel:
            return ""
        return next(iter(min_node.keys))




# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
