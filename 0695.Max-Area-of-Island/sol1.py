from collections import deque


class Solution:
    LAND = 1
    WATER = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        def inside_grid(pos):
            i, j = pos
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def generate_adjacent(pos):
            i, j = pos
            for delta in [1, -1]:
                if inside_grid((i + delta, j)):
                    yield (i + delta, j)
                if inside_grid((i, j + delta)):
                    yield (i, j + delta)

        def bfs(pos, visited):
            que = deque()
            que.append(pos)
            visited[pos[0]][pos[1]] = True
            area = 0
            while que:
                curr_pos = que.popleft()
                area += 1
                for i, j in generate_adjacent(curr_pos):
                    if grid[i][j] == self.LAND and not visited[i][j]:
                        visited[i][j] = True
                        que.append((i, j))
            return area

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        area_max = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.WATER or visited[i][j]:
                    continue
                area = bfs((i, j), visited)
                area_max = max(area, area_max)
        return area_max
