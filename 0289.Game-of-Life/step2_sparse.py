import itertools
import collections

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])
        live_cells = set()
        for r, c in itertools.product(range(num_rows), range(num_cols)):
            if board[r][c] == 1:
                 live_cells.add((r, c))

        counts = collections.defaultdict(int)
        for r, c in list(live_cells):
            for next_r, next_c in ((r + dr, c + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if not (dr == 0 and dc == 0)):
                if not (0 <= next_r < num_rows and 0 <= next_c < num_cols):
                    continue
                counts[(next_r, next_c)] += 1

        next_live_cells = set()
        for (r, c), count in counts.items():
            if count == 3 or (count == 2 and (r, c) in live_cells):
                next_live_cells.add((r, c))

        live_cells = next_live_cells

        for r, c in itertools.product(range(num_rows), range(num_cols)):
            if (r, c) in live_cells:
                board[r][c] = 1
            else:
                board[r][c] = 0

