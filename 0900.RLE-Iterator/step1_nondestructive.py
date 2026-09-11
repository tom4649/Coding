class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.index = 0
        self.offset = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding) - 1:
            remaining = self.encoding[self.index] - self.offset

            if remaining < n:
                n -= remaining
                self.index += 2
                self.offset = 0
            else:
                self.offset += n
                return self.encoding[self.index + 1]

        return -1
