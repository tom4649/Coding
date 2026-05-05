# テストケースで失敗
import functools


class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def num_ways(self, n: int, k: int) -> int:
        @functools.cache
        def num_ways_helper(m):
            if m == 1:
                return k
            if m == 2:
                return k * k
            return (k - 1) * (num_ways_helper(m - 2) + num_ways_helper(m - 1))

        return num_ways_helper(n)
