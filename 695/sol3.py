from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.area = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def add(self, x):
        self.area[x] = 1

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        # union by size (area)
        if self.area[root_x] < self.area[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.area[root_x] += self.area[root_y]
        self.area[root_y] = 0


class Solution:
    LAND = 1
    WATER = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def generate_if_inside_grid(pos):
            i, j = pos
            if 0 <= i < rows and 0 <= j < cols:
                yield (i, j)

        def generate_adjacent_one_side(pos):
            i, j = pos
            yield from generate_if_inside_grid((i + 1, j))
            yield from generate_if_inside_grid((i, j + 1))

        def idx(i, j):
            return i * cols + j

        uf = UnionFind(rows * cols)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == self.LAND:
                    uf.add(idx(i, j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == self.WATER:
                    continue
                for i_next, j_next in generate_adjacent_one_side((i, j)):
                    if grid[i_next][j_next] == self.LAND:
                        uf.union(idx(i, j), idx(i_next, j_next))
        return max(uf.area)
