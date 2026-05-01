class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = 0

    def add(self, x):
        self.parent[x] = x
        self.size[x] = 1
        self.count += 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True


class Solution:
    WATER = "0"
    LAND = "1"

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        def idx(i, j):
            return i * n + j

        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.LAND:
                    uf.add(idx(i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] != self.LAND:
                    continue
                if i + 1 < m and grid[i + 1][j] == self.LAND:
                    uf.union(idx(i, j), idx(i + 1, j))
                if j + 1 < n and grid[i][j + 1] == self.LAND:
                    uf.union(idx(i, j), idx(i, j + 1))

        return uf.count
