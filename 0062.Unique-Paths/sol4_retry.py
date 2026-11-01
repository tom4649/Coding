from itertools import count


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            n, m = m, n

        count_unque_paths = 1
        for i in range(n + m - 2, m - 1, -1):
            count_unque_paths *= i
        for i in range(n - 1, 1, -1):
            count_unque_paths //= i

        return count_unque_paths
