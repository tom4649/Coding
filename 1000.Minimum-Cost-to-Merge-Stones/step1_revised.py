import itertools
import math

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        num_stones = len(stones)
        if (num_stones - 1) % (k - 1) != 0:
            return -1

        prefix_sum = list(itertools.accumulate(stones, initial=0))

        min_cost = [[[float("inf")] * (k + 1) for _ in range(num_stones)] for _ in range(num_stones)]

        for left in range(num_stones):
            min_cost[left][left][1] = 0

        for length in range(2, num_stones + 1):
            for left in range(num_stones - length + 1):
                right = left + length - 1
                for num_pile in range(2, min(k, length) + 1):
                    for mid in range(left, right):
                        min_cost[left][right][num_pile] = min(
                            min_cost[left][right][num_pile],
                            min_cost[left][mid][1] + min_cost[mid + 1][right][num_pile - 1]
                        )

                if not math.isinf(min_cost[left][right][k]):
                    min_cost[left][right][1] = min_cost[left][right][k] + prefix_sum[right + 1] - prefix_sum[left]

        return min_cost[0][-1][1]
