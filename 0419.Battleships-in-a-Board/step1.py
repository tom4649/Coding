import itertools
import collections

BATTLESHIP = "X"

class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]
        num_battleships = 0

        for i, j in itertools.product(range(n), range(m)):
            if visited[i][j]:
                continue
            visited[i][j] = True
            if board[i][j] != BATTLESHIP:
                continue
            battleship = []
            component = collections.deque([(i, j)])
            while component:
                r, c = component.popleft()
                for r_next, c_next in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if not (0 <= r_next < n and 0 <= c_next < m):
                        continue
                    if visited[r_next][c_next]:
                        continue
                    visited[r_next][c_next] = True
                    if board[r_next][c_next] != BATTLESHIP:
                        continue
                    component.append((r_next, c_next))

            num_battleships += 1

        return num_battleships

