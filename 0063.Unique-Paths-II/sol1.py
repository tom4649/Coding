class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        num_rows, num_cols = len(obstacleGrid), len(obstacleGrid[0])

        EMPTY = 0

        if obstacleGrid[0][0] != EMPTY:
            return 0

        unique_paths_per_row = [1] + [0] * (num_cols - 1)

        col = 1
        while col < num_cols and obstacleGrid[0][col] == EMPTY:
            unique_paths_per_row[col] = 1
            col += 1

        for row in range(1, num_rows):
            for col in range(0, num_cols):
                if obstacleGrid[row][col] != EMPTY:
                    unique_paths_per_row[col] = 0
                    continue
                if col == 0:
                    continue
                unique_paths_per_row[col] += unique_paths_per_row[col - 1]

        return unique_paths_per_row[-1]
