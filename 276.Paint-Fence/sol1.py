class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k
        num_duplicated = k
        num_non_duplicated = k * (k - 1)
        for _ in range(n - 2):
            num_duplicated, num_non_duplicated = num_non_duplicated, (
                num_duplicated + num_non_duplicated
            ) * (k - 1)
        return num_duplicated + num_non_duplicated
