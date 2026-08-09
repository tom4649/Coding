class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_weight = 0
        while n > 0:
            hamming_weight += n & 1
            n >>= 1
        return hamming_weight

