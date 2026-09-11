class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding) - 1:
            if self.encoding[self.index] < n:
                n -= self.encoding[self.index]
                self.index += 2
            else:
                self.encoding[self.index] -= n
                return self.encoding[self.index + 1]

        return -1
