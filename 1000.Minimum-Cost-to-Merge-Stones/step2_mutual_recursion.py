from functools import cache
import itertools

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        num_stones = len(stones)
        if (num_stones - 1) % (k - 1) != 0:
            return -1

        @cache
        def min_reduce_cost(i, j):
            if i == j:
                return 0

            minimum = float("inf")
            for mid in range(i, j, k - 1):
                right_len = j - (mid + 1) + 1
                if (right_len - 1) % (k - 1) == 0:
                    right_cost = min_merge_cost(mid + 1, j)
                else:
                    right_cost = min_reduce_cost(mid + 1, j)

                minimum = min(minimum, min_merge_cost(i, mid) + right_cost)

            return minimum

        prefix_sum = list(itertools.accumulate(stones, initial=0))

        @cache
        def min_merge_cost(i, j):
            length = j - i + 1

            if length == 1:
                return 0

            if (length - 1) % (k - 1) != 0:
                return float("inf")

            base_cost = min_reduce_cost(i, j)
            if base_cost == float("inf"):
                return float("inf")

            return base_cost + prefix_sum[j + 1] - prefix_sum[i]

        return min_merge_cost(0, num_stones - 1)
