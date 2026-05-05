class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        num_flip = 0
        half_length = 2 ** (n - 2)
        while half_length > 0:
            if k > half_length:
                num_flip += 1
                k -= half_length
            half_length //= 2
        assert k == 1
        return num_flip % 2
