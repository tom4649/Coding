class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        adjacent = [[] for _ in range(n)]

        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= ri ** 2:
                    adjacent[i].append(j)

        reachable = [[False] * n for _ in range(n)]
        def traverse_from(start):
            detonated = [start]
            visited = {start}
            reachable[start][start] = True
            while detonated:
                i = detonated.pop()
                for j in adjacent[i]:
                    if j in visited:
                        continue
                    visited.add(j)
                    detonated.append(j)
                    reachable[start][j] = True

        for i in range(n):
            traverse_from(i)

        return max(sum(reachable[i]) for i in range(n))
