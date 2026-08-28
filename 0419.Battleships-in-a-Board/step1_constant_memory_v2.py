class Solution:

    def countBattleships(self, board: list[list[str]]) -> int:
        n = len(board)
        m = len(board[0])
        num_battleships = 0

        for i in range(n):
            for j in range(m):
                if board[i][j] != "X":
                    continue
                if i > 0 and board[i - 1][j] == "X":
                    continue
                if j > 0 and board[i][j - 1] == "X":
                    continue

                num_battleships += 1

        return num_battleships
