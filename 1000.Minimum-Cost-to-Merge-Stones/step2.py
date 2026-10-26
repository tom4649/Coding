import itertools

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        num_stones = len(stones)
        if (num_stones - 1) % (k - 1) != 0:
            return -1

        prefix_sum = list(itertools.accumulate(stones, initial=0))

        dp = [[0] * num_stones for _ in range(num_stones)]

        for length in range(2, num_stones + 1):
            for i in range(num_stones - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")

                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])

                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix_sum[j + 1] - prefix_sum[i]

        return dp[0][-1]

