class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k
        num_before_last = k
        num_last = k * k

        for _ in range(n - 2):
            num_before_last, num_last = num_last, (k - 1) * (num_before_last + num_last)
        return num_last
