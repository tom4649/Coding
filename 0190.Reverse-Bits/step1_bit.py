class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0
        num_bits = 0
        while num_bits < 32:
            reversed_bits <<= 1
            reversed_bits |= n & 1
            n >>= 1
            num_bits += 1
        return reversed_bits


