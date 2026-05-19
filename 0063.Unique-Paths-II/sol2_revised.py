class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        n_row, n_col = len(obstacleGrid), len(obstacleGrid[0])

        unique_paths_per_row = [0] * n_col
        if obstacleGrid[0][0] == 1:
            return 0
        unique_paths_per_row[0] = 1

        for row in range(n_row):
            for col in range(n_col):
                if obstacleGrid[row][col]:
                    unique_paths_per_row[col] = 0
                elif col > 0:
                    unique_paths_per_row[col] += unique_paths_per_row[col - 1]

        return unique_paths_per_row[-1]
