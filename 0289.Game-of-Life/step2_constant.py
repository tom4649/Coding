import itertools

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])
        for r, c in itertools.product(range(num_rows), range(num_cols)):
            num_live_neighbors = 0
            for next_r, next_c in ((r + dr, c + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if not (dr == 0 and dc == 0)):
                if not (0 <= next_r < num_rows and 0 <= next_c < num_cols):
                    continue
                num_live_neighbors += board[next_r][next_c] & 1

            if board[r][c] & 1 and 2 <= num_live_neighbors <= 3:
                    board[r][c] |= 2
            elif num_live_neighbors == 3:
                    board[r][c] |= 2

        for r, c in itertools.product(range(num_rows), range(num_cols)):
            board[r][c] >>=  1

