class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_weight = 0
        while n > 0:
            n &= n - 1
            hamming_weight += 1
        return hamming_weight

