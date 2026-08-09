class Solution:
    REVERSE_TABLE = [0] * 256

    @classmethod
    def init_table(cls):
        for i in range(1, 256):
            cls.REVERSE_TABLE[i] = (cls.REVERSE_TABLE[i >> 1] >> 1) | ((i & 1) << 7)

    def __init__(self):
        if self.REVERSE_TABLE[1] == 0:
            self.init_table()

    def reverseBits(self, n: int) -> int:
        n = n & 0xffffffff

        byte0 = self.REVERSE_TABLE[n & 0xff]
        byte1 = self.REVERSE_TABLE[(n >> 8) & 0xff]
        byte2 = self.REVERSE_TABLE[(n >> 16) & 0xff]
        byte3 = self.REVERSE_TABLE[(n >> 24) & 0xff]

        return (byte0 << 24) | (byte1 << 16) | (byte2 << 8) | byte3