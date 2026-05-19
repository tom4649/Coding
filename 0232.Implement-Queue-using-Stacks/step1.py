class MyQueue:
    def __init__(self):
        self.data = []
        self.data_reversed = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        if self.empty():
            raise RuntimeError("myque is empty")
        self._reverse()
        return self.data_reversed.pop()

    def peek(self) -> int:
        if self.empty():
            raise RuntimeError("myque is empty")
        self._reverse()
        return self.data_reversed[-1]

    def empty(self) -> bool:
        return not self.data and not self.data_reversed

    def _reverse(self) -> None:
        if not self.data_reversed:
            while self.data:
                self.data_reversed.append(self.data.pop())
