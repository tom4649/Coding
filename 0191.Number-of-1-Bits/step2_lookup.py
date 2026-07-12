class Solution:
    WORDBITS = [0] * 65536

    @classmethod
    def init_wordbits(cls):
        for i in range(1, len(cls.WORDBITS)):
            cls.WORDBITS[i] = cls.WORDBITS[i >> 1] + (i & 1)

    def __init__(self):
        if self.WORDBITS[1] == 0:
            self.init_wordbits()

    def hammingWeight(self, n: int) -> int:
        n = n & 0xffffffff
        return self.WORDBITS[n & 0xffff] + self.WORDBITS[n >> 16]