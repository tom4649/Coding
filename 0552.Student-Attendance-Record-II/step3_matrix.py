MODULO = 10**9 + 7

class Solution:
    def checkRecord(self, n: int) -> int:
        base_matrix = [
            [1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            ]

        transformed_matrix =  [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            ]

        def multiply_matrices(A, B):
            return [
                [sum((A[i][j] * B[j][k] for j in range(len(A[0])))) % MODULO for k in range(len(B[0]))]
                for i in range(len(A))
            ]

        power = n - 1
        while power > 0:
            if power % 2 == 1:
                transformed_matrix = multiply_matrices(base_matrix, transformed_matrix)

            base_matrix = multiply_matrices(base_matrix, base_matrix)
            power //= 2

        initial_state_vector = [[1], [1], [0], [1], [0], [0]]
        final_state_vector = multiply_matrices(transformed_matrix, initial_state_vector)

        return sum(final_state_vector[i][0] for i in range(len(final_state_vector))) % MODULO
