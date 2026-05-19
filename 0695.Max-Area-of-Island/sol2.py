from collections import deque


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

        def generate_adjacent(pos):
            i, j = pos
            yield from generate_if_inside_grid((i + 1, j))
            yield from generate_if_inside_grid((i - 1, j))
            yield from generate_if_inside_grid((i, j + 1))
            yield from generate_if_inside_grid((i, j - 1))

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

        visited = [[False] * cols for _ in range(rows)]
        area_max = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == self.WATER or visited[i][j]:
                    continue
                area = bfs((i, j), visited)
                area_max = max(area, area_max)
        return area_max
