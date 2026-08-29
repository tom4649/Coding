class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points or not points[0]:
            return 0

        num_rows = len(points)
        num_cols = len(points[0])

        previous_max_points = points[0][:]
        max_points = [0] * num_cols

        for r in range(1, num_rows):
            running_max = 0
            for c in range(num_cols):
                running_max = max(running_max - 1, previous_max_points[c])
                max_points[c] = running_max

            running_max = 0
            for c in range(num_cols - 1, -1, -1):
                running_max = max(running_max - 1, previous_max_points[c])
                max_points[c] = max(running_max, max_points[c]) + points[r][c]

            max_points, previous_max_points = previous_max_points, max_points

        return max(previous_max_points)

