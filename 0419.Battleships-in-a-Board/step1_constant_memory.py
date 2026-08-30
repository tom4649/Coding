BATTLESHIP = "X"

class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        n = len(board)
        m = len(board[0])
        num_battleships = 0

        for i in range(n):
            j = 0
            while j < m:
                if board[i][j] != BATTLESHIP:
                    j += 1
                    continue
                if (i > 0 and board[i - 1][j] == BATTLESHIP) or (i < n - 1 and  board[i + 1][j] == BATTLESHIP):
                    j += 1
                    continue
                num_battleships += 1
                while j < m and board[i][j] == BATTLESHIP:
                    j += 1

        for j in range(m):
            i = 0
            while i < n:
                if board[i][j] != BATTLESHIP:
                    i += 1
                    continue
                if i == n - 1 or board[i+1][j] != BATTLESHIP:
                    i += 1
                    continue
                num_battleships += 1
                while i < n and board[i][j] == BATTLESHIP:
                    i += 1

        return num_battleships




