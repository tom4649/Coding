import itertools

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])
        changed_cells = []
        for r, c in itertools.product(range(num_rows), range(num_cols)):
            num_live_neighbors = 0
            for next_r, next_c in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r + 1, c + 1), (r + 1, c - 1), (r - 1, c + 1), (r - 1, c - 1)):
                if not (0 <= next_r < num_rows and 0 <= next_c < num_cols):
                    continue
                num_live_neighbors += board[next_r][next_c]

            if board[r][c] == 1:
                if num_live_neighbors < 2 or num_live_neighbors > 3:
                    changed_cells.append((r, c))
            else:
                if num_live_neighbors == 3:
                    changed_cells.append((r, c))

        for r, c in changed_cells:
            board[r][c] = 1 - board[r][c]

