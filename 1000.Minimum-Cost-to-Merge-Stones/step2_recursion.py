from functools import cache
import itertools

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        num_stones = len(stones)
        if (num_stones - 1) % (k - 1) != 0:
            return -1

        prefix_sum = list(itertools.accumulate(stones, initial=0))

        @cache
        def min_cost(i, j):
            if i == j:
                return 0

            minimum = float("inf")
            for mid in range(i, j, k - 1):
                minimum = min(minimum, min_cost(i, mid) + min_cost(mid + 1, j))

            length = j - i + 1
            if (length - 1) % (k - 1) == 0:
                minimum += prefix_sum[j + 1] - prefix_sum[i]

            return minimum

        return min_cost(0, num_stones - 1)
