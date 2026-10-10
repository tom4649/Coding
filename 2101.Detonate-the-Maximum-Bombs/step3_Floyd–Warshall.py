class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        num_bombs = len(bombs)
        reachable = [[False] * num_bombs for _ in range(num_bombs)]

        for i in range(num_bombs):
            reachable[i][i] = True
            xi, yi, ri = bombs[i]
            for j in range(num_bombs):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                reachable[i][j] = (xi - xj) ** 2 + (yi - yj) ** 2 <= ri ** 2

        for k in range(num_bombs):
            for i in range(num_bombs):
                for j in range(num_bombs):
                    reachable[i][j] |= reachable[i][k] and reachable[k][j]

        return max(sum(reachable[i]) for i in range(num_bombs))
