import itertools


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            raise ValueError("invalid board")

        num_row = len(board)
        num_col = len(board[0])

        def traverse(row: int, col: int, i: int, seen: list[list][bool]) -> bool:
            if not word[i] == board[row][col]:
                return False
            if i == len(word) - 1:
                return True
            for row_next, col_next in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if (
                    0 <= row_next < num_row
                    and 0 <= col_next < num_col
                    and not seen[row_next][col_next]
                ):
                    seen[row_next][col_next] = True
                    if traverse(row_next, col_next, i + 1, seen):
                        return True
                    seen[row_next][col_next] = False

            return False

        for row, col in itertools.product(range(num_row), range(num_col)):
            seen = [[False] * num_col for _ in range(num_row)]
            seen[row][col] = True
            if traverse(row, col, 0, seen):
                return True

        return False
