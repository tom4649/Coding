BATTLESHIP = "X"

class Solution:

    def countBattleships(self, board: list[list[str]]) -> int:
        num_rows = len(board)
        num_cols = len(board[0])
        num_battleships = 0

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] != BATTLESHIP:
                    continue

                if r > 0 and board[r - 1][c] == BATTLESHIP:
                    continue

                if c > 0 and board[r][c - 1] == BATTLESHIP:
                    continue

                num_battleships += 1

        return num_battleships
