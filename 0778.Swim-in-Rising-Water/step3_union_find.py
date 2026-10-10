class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        self.parent[root_x] = root_y
        return True



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
                    edges.append((cost, r * n + c, (r + 1) * n + c))
                if c + 1 < n:
                    cost = max(grid[r][c], grid[r][c + 1])
                    edges.append((cost, r * n + c, r * n + c + 1))

        edges.sort()

        uf = UnionFind(n * n)

        for cost, u, v in edges:
            uf.union(u, v)
            if uf.find(0) == uf.find((n - 1) * n + n - 1):
                return cost


