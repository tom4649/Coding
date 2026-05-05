class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        num_char = 2 ** (n - 1)
        if k <= 0 or k > num_char:
            raise ValueError(f"Invalid input k: {k}, n: {n}")
        if n == 1:
            return 0
        if k > num_char // 2:
            return 1 - self.kthGrammar(n - 1, k - num_char // 2)
        return self.kthGrammar(n - 1, k)
