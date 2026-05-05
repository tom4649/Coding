from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(maxsize=None)
        def count_unique_paths(a, b):
            if a == 1 or b == 1:
                return 1
            return count_unique_paths(a - 1, b) + count_unique_paths(a, b - 1)

        return count_unique_paths(m, n)
