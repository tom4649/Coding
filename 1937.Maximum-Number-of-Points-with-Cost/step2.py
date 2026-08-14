class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points or not points[0]:
            return 0

        num_rows = len(points)
        num_cols = len(points[0])

        dp_prev = points[0][:]
        dp = [0] * num_cols

        for r in range(1, num_rows):
            left = [0] * num_cols
            left[0] = dp_prev[0]
            for c in range(1, num_cols):
                left[c] = max(left[c - 1] - 1, dp_prev[c])

            right = [0] * num_cols
            right[-1] = dp_prev[-1]
            for c in range(num_cols - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, dp_prev[c])

            for c in range(num_cols):
                dp[c] = points[r][c] + max(left[c], right[c])

            dp_prev, dp = dp, dp_prev

        return max(dp_prev)
