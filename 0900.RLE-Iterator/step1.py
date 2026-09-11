class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.index = 0


    def next(self, n: int) -> int:
        next_value = -1
        while n > 0 and self.index <= len(self.encoding) - 2:
            if self.encoding[self.index] < n:
                n -= self.encoding[self.index]
                self.index += 2
            else:
                next_value = self.encoding[self.index + 1]
                self.encoding[self.index] -= n
                n = 0

        return next_value







# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
