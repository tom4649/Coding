OBSTACLE = 1


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        n_col = len(obstacleGrid[0])
        count_paths_per_row = [0] * n_col
        count_paths_per_row[0] = 1

        for row in obstacleGrid:
            for i_col, window in enumerate(row):
                if window == OBSTACLE:
                    count_paths_per_row[i_col] = 0
                    continue
                if i_col > 0:
                    count_paths_per_row[i_col] += count_paths_per_row[i_col - 1]

        return count_paths_per_row[-1]
