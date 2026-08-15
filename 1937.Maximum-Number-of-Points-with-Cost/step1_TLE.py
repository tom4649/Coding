class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points or not points[0]:
            return 0

        num_rows = len(points)
        num_cols = len(points[0])

        dp_prev = points[0][:]
        dp = [0] * num_cols

        for r in range(1, num_rows):
            for c in range(num_cols):
                dp[c] = max([dp_prev[c_prev] - abs(c - c_prev) for c_prev in range(num_cols)]) + points[r][c]
            dp, dp_prev = dp_prev, dp

        return max(dp_prev)


