class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        unique_paths_per_row = [1 - o for o in obstacleGrid[0]]
        for col in range(1, n):
            unique_paths_per_row[col] *= unique_paths_per_row[col - 1]

        for row in range(1, m):
            for col in range(0, n):
                if obstacleGrid[row][col]:
                    unique_paths_per_row[col] = 0
                    continue
                if col == 0:
                    continue
                unique_paths_per_row[col] += unique_paths_per_row[col - 1]

        return unique_paths_per_row[-1]
