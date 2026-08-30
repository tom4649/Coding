class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        reachable = [[False] * n for _ in range(n)]

        for i in range(n):
            reachable[i][i] = True
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= ri ** 2:
                    reachable[i][j] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

        return max(sum(reachable[i]) for i in range(n))
