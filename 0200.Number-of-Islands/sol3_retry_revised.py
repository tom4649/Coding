from typing import List

LAND = "1"
WATER = "0"
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        def is_inside(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols

        def is_land(row, col):
            return is_inside(row, col) and grid[row][col] == LAND

        def iter_neighbors(row, col):
            for d_row, d_col in DIRECTIONS:
                yield row + d_row, col + d_col

        num_islands = 0
        seen = set()

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == WATER or (row, col) in seen:
                    continue

                frontier = [(row, col)]
                seen.add((row, col))

                while frontier:
                    cur_row, cur_col = frontier.pop()

                    for next_row, next_col in iter_neighbors(cur_row, cur_col):
                        if (next_row, next_col) in seen or not is_land(next_row, next_col):
                            continue
                        seen.add((next_row, next_col))
                        frontier.append((next_row, next_col))

                num_islands += 1
        return num_islands
