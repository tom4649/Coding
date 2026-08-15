class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points or not points[0]:
            return 0

        num_rows = len(points)
        num_cols = len(points[0])

        dp_prev = points[0][:]
        dp = [0] * num_cols

        for r in range(1, num_rows):
            running_max = 0
            for c in range(num_cols):
                running_max = max(running_max - 1, dp_prev[c])
                dp[c] = running_max

            running_max = 0
            for c in range(num_cols - 1, -1, -1):
                running_max = max(running_max - 1, dp_prev[c])
                dp[c] = max(dp[c], running_max) + points[r][c]

            dp_prev, dp = dp, dp_prev

        return max(dp_prev)
