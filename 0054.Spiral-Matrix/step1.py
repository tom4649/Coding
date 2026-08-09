class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not (matrix and matrix[0]):
            raise ValueError("matrix is empty")

        num_row = len(matrix)
        num_col = len(matrix[0])

        added_row_min = -1
        added_row_max = num_row
        added_col_min = -1
        added_col_max = num_col
        row = 0
        col = -1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx_direction = 0
        result = []

        while added_row_min + 1 < added_row_max and added_col_min + 1 < added_col_max:
            direction = directions[idx_direction % 4]
            while True:
                row += direction[0]
                col += direction[1]
                result.append(matrix[row][col])

                if direction == (0, 1) and col == added_col_max - 1:
                    added_row_min = row
                    break
                if direction == (1, 0) and row == added_row_max - 1:
                    added_col_max = col
                    break
                if direction == (0, -1) and col == added_col_min + 1:
                    added_row_max = row
                    break
                if direction == (-1, 0) and row == added_row_min + 1:
                    added_col_min = col
                    break
            idx_direction += 1

        return result
