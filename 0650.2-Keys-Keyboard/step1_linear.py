class Solution:
    def minSteps(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[1] = 0

        for num_to_make in range(2, n + 1):
            dp[num_to_make] = num_to_make

            for num_to_paste in range(num_to_make // 2, 1, -1):
                if num_to_make % num_to_paste == 0:
                    dp[num_to_make] = dp[num_to_paste] + (num_to_make // num_to_paste)
                    break

        return dp[n]
