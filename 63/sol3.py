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

                ways = unique_paths_per_row[col]
                if ways == 0:
                    continue

                if col + 1 < n_col and not obstacleGrid[row][col + 1]:
                    unique_paths_per_row[col + 1] += ways
                if row + 1 < n_row and not obstacleGrid[row + 1][col]:
                    unique_paths_next_row[col] += ways

            if row + 1 < n_row:
                unique_paths_per_row = unique_paths_next_row

        return unique_paths_per_row[-1]
