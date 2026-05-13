import itertools


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not (mat and mat[0]):
            raise ValueError("mat is empty")

        num_row = len(mat)
        num_col = len(mat[0])

        result = [[-1] * num_col for _ in range(num_row)]
        frontier = []
        for row, col in itertools.product(range(num_row), range(num_col)):
            if mat[row][col] == 0:
                frontier.append((row, col))
                result[row][col] = 0

        distance = 1
        while frontier:
            next_frontier = []
            for row, col in frontier:
                for next_row, next_col in (
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1),
                ):
                    if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                        continue
                    if result[next_row][next_col] != -1:
                        continue
                    next_frontier.append((next_row, next_col))
                    result[next_row][next_col] = distance
            frontier = next_frontier
            distance += 1

        return result
