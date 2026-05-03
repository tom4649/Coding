class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        def inside_grid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def get_adjacent(pos):
            i = pos[0]
            j = pos[1]
            for delta in [1, -1]:
                if inside_grid(i + delta, j):
                    yield (i + delta, j)
                if inside_grid(i, j + delta):
                    yield (i, j + delta)

        def dfs(pos, grid):
            grid[pos[0]][pos[1]] = "0"
            for i, j in get_adjacent(pos):
                if grid[i][j] == "1":
                    grid = dfs((i, j), grid)
            return grid

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid = dfs((i, j), grid)
                    count += 1
        return count
