class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n < m:
            m, n = n, m

        unique_paths_per_row = [1] * m

        for _ in range(1, n):
            for col in range(1, m):
                unique_paths_per_row[col] += unique_paths_per_row[col - 1]

        return unique_paths_per_row[-1]
