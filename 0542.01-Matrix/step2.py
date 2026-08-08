class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not (mat and mat[0]):
            raise ValueError("mat is empty")

        num_row = len(mat)
        num_col = len(mat[0])
        max_dist = num_row + num_col

        result = [[0] * num_col for _ in range(num_row)]
        for row in range(num_row):
            for col in range(num_col):
                if mat[row][col] == 0:
                    continue
                result[row][col] = max_dist
                if row > 0:
                    result[row][col] = min(result[row][col], result[row - 1][col] + 1)
                if col > 0:
                    result[row][col] = min(result[row][col], result[row][col - 1] + 1)

        for row in range(num_row - 1, -1, -1):
            for col in range(num_col - 1, -1, -1):
                if mat[row][col] == 0:
                    continue
                if row + 1 < num_row:
                    result[row][col] = min(result[row][col], result[row + 1][col] + 1)
                if col + 1 < num_col:
                    result[row][col] = min(result[row][col], result[row][col + 1] + 1)

        return result
