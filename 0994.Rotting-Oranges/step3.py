from enum import IntEnum
import math
import itertools


class Orange(IntEnum):
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        rotten_minutes = [[math.inf] * num_cols for _ in range(num_rows)]
        frontier = []

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if grid[row][col] == Orange.ROTTEN:
                frontier.append((row, col, 0))
            elif grid[row][col] == Orange.EMPTY:
                rotten_minutes[row][col] = 0

        while frontier:
            row, col, elapsed = frontier.pop()
            if (
                not (0 <= row < num_rows and 0 <= col < num_cols)
                or grid[row][col] == Orange.EMPTY
            ):
                continue
            if rotten_minutes[row][col] <= elapsed:
                continue
            rotten_minutes[row][col] = elapsed
            for next_row, next_col in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                frontier.append((next_row, next_col, elapsed + 1))

        max_minute = max(max(row) for row in rotten_minutes)

        return max_minute if not math.isinf(max_minute) else -1
