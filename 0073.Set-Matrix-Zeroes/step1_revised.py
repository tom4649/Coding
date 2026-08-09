class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row_with_zero = set()
        column_with_zero = set()

        for r, row in enumerate(matrix):
            for c, value in enumerate(row):
                if value == 0:
                    row_with_zero.add(r)
                    column_with_zero.add(c)

        for r, row in enumerate(matrix):
            if r in row_with_zero:
                row[:] = [0] * len(row)
                continue
            for c in column_with_zero:
                row[c] = 0
