class MinStack:
    def __init__(self):
        self.data = []
        self.min_data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.data) > 1:
            val_min = self.getMin()
        else:
            val_min = val
        if val_min > val:
            val_min = val
        self.min_data.append(val_min)

    def pop(self) -> None:
        if not self.data:
            raise IndexError("pop from empty stack")
        self.data.pop()
        self.min_data.pop()

    def top(self) -> int:
        if not self.data:
            raise IndexError("top from empty stack")
        return self.data[-1]

    def getMin(self) -> int:
        if not self.min_data:
            raise IndexError("getMin from empty stack")
        return self.min_data[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
