# https://github.com/nittoco/leetcode/pull/49/changes

import math


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        m, n = len(grid), len(grid[0])
        rotting_minutes = [[math.inf] * n for _ in range(m)]

        def update_minute(row: int, col: int, minute: int) -> None:
            if not (0 <= row < m and 0 <= col < n):
                return
            if grid[row][col] == EMPTY:
                return
            if minute > rotting_minutes[row][col]:
                return
            rotting_minutes[row][col] = minute
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dirs:
                update_minute(row + dr, col + dc, minute + 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == EMPTY:
                    rotting_minutes[row][col] = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == ROTTEN:
                    update_minute(row, col, 0)
        max_minutes = 0
        for row in range(m):
            for col in range(n):
                max_minutes = max(max_minutes, rotting_minutes[row][col])

        return max_minutes if not math.isinf(max_minutes) else -1
