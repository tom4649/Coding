class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = 1
        if m < n:
            m, n = n, m

        for i in range(m, m + n - 1):
            total *= i

        for i in range(1, n):
            total //= i

        return total
