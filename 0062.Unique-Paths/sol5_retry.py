import functools

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.cache
        def unique_paths_helper(num_rows, num_cols):
            if num_rows > num_cols:
                num_rows, num_cols = num_cols, num_rows
            if num_rows == 1:
                return 1

            num_unique_paths = 0
            for i in range(num_cols):
                num_unique_paths += unique_paths_helper(num_rows - i, num_cols - 1)

            return num_unique_paths

        return unique_paths_helper(m, n)
