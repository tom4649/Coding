class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        n_row, n_col = len(obstacleGrid), len(obstacleGrid[0])

        unique_paths_per_row = [0] * n_col
        unique_paths_per_row[0] = 0 if obstacleGrid[0][0] else 1

        for row in range(n_row):
            unique_paths_next_row = [0] * n_col
            for col in range(n_col):
                if obstacleGrid[row][col]:
                    unique_paths_per_row[col] = 0
                    continue

                paths = unique_paths_per_row[col]
                if paths == 0:
                    continue

                if col + 1 < n_col:
                    unique_paths_per_row[col + 1] += paths
                if row + 1 < n_row:
                    unique_paths_next_row[col] += paths

            if row + 1 < n_row:
                unique_paths_per_row = unique_paths_next_row

        return unique_paths_per_row[-1]
