class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        if len(matrix) != len(matrix[0]):
            raise ValueError("matrix is invalid")

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()

