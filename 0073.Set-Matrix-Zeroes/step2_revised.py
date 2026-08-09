class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = 0 in matrix[0]
        first_column_has_zero = any(matrix[r][0] == 0 for r in range(m))

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_has_zero:
            matrix[0][:] = [0] * n

        if first_column_has_zero:
            for r in range(m):
                matrix[r][0] = 0
