import itertools

LAND = "1"
WATER = "0"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not (grid and grid[0]):
            raise ValueError("Invalid grid")

        def inside_land(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                return False
            if grid[x][y] == WATER:
                return False
            return True

        num_islands = 0
        seen = set()

        for x, y in itertools.product(range(len(grid)), range(len(grid[0]))):
            if grid[x][y] == WATER or (x, y) in seen:
                continue

            frontier = [(x, y)]
            while frontier:
                x_cur, y_cur = frontier.pop()
                seen.add((x_cur, y_cur))
                if grid[x_cur][y_cur] == WATER:
                    continue
                assert grid[x_cur][y_cur] == LAND

                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x_next, y_next = x_cur + dx, y_cur + dy
                    if (x_next, y_next) not in seen and inside_land(x_next, y_next):
                        frontier.append((x_next, y_next))
            num_islands += 1
        return num_islands
