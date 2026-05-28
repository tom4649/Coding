import math


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [[math.inf] * (n + 1) for _ in range(n + 1)]
        dp[1][0] = 0
        for i in range(1, n + 1):
            min_i = math.inf if i != 1 else 0
            for j in range(1, i + 1):
                if 2 * j <= i:
                    dp[i][j] = dp[i - j][j] + 1
                    min_i = min(min_i, dp[i][j])
            dp[i][i] = min_i + 1

        return min(dp[n])
