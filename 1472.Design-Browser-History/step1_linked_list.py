class Node:

    def __init__(self, val: str):
        self.val = val
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.node = Node(homepage)

    def visit(self, url: str) -> None:
        next_node = Node(url)
        self.node.next = next_node
        next_node.prev = self.node
        self.node = next_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.node.prev:
            self.node = self.node.prev
            steps -= 1
        return self.node.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.node.next:
            self.node = self.node.next
            steps -= 1
        return self.node.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
