class Solution:

    def countBattleships(self, board: list[list[str]]) -> int:
        n = len(board)
        m = len(board[0])
        num_battleships = 0

        for r in range(n):
            for c in range(m):
                if board[r][c] != "X":
                    continue
                if r > 0 and board[r - 1][c] == "X":
                    continue
                if c > 0 and board[r][c - 1] == "X":
                    continue

                num_battleships += 1

        return num_battleships
