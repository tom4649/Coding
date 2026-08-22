class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        if len(grid) != len(grid[0]):
            raise ValueError("invalid grid")
        if len(grid) == 1:
            return grid[0][0]

        n = len(grid)

        edges = []
        for r in range(n):
            for c in range(n):
                if r + 1 < n:
                    cost = max(grid[r][c], grid[r + 1][c])
                    edges.append((cost, r * n + c, (r + 1)* n + c))
                if c + 1 < n:
                    cost = max(grid[r][c], grid[r][c + 1])
                    edges.append((cost, r * n + c, r * n + c + 1))

        edges.sort()

        uf = UnionFind(n * n)

        for cost, u, v in edges:
            uf.union(u, v)
            if uf.find(0) == uf.find((n - 1) * n + n - 1):
                return cost

        return -1
