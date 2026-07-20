class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row_with_zero = set()
        column_with_zero = set()

        for index_row, row in enumerate(matrix):
            for index_column, value in enumerate(row):
                if value == 0:
                    row_with_zero.add(index_row)
                    column_with_zero.add(index_column)

        for index_row, row in enumerate(matrix):
            if index_row in row_with_zero:
                row[:] = [0] * len(row)
                continue
            for index_column in column_with_zero:
                row[index_column] = 0
