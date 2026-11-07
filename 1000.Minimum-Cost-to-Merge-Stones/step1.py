import itertools
import math

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        num_stones = len(stones)
        if (num_stones - 1) % (k - 1) != 0:
            return -1

        prefix_sum = list(itertools.accumulate(stones, initial=0))

        dp = [[[float("inf")] * (k + 1) for _ in range(num_stones)] for _ in range(num_stones)]

        for i in range(num_stones):
            dp[i][i][1] = 0

        for length in range(2, num_stones + 1):
            for i in range(num_stones - length + 1):
                j = i + length - 1
                for num_pile in range(2, min(k, length) + 1):
                    for mid in range(i, j):
                        dp[i][j][num_pile] = min(dp[i][j][num_pile], dp[i][mid][1] + dp[mid + 1][j][num_pile - 1])

                if not math.isinf(dp[i][j][k]):
                    dp[i][j][1] = dp[i][j][k] + prefix_sum[j+1] - prefix_sum[i]

        return dp[0][-1][1]





