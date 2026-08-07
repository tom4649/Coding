import itertools

EMPTY = 0
FRESH = 1
ROTTEN = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])

        def generate_adjacent_to(row, col):
            for next_row, next_col in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if 0 <= next_row < num_row and 0 <= next_col < num_col:
                    yield (next_row, next_col)

        fresh = set()
        rotten_queue = []
        for row, col in itertools.product(range(num_row), range(num_col)):
            if grid[row][col] == ROTTEN:
                rotten_queue.append((row, col))
            elif grid[row][col] == FRESH:
                fresh.add((row, col))

        elapsed = 0
        while fresh and rotten_queue:
            next_rotten = []
            for row, col in rotten_queue:
                for next_row, next_col in generate_adjacent_to(row, col):
                    if (next_row, next_col) in fresh:
                        fresh.remove((next_row, next_col))
                        next_rotten.append((next_row, next_col))
            elapsed += 1
            rotten_queue = next_rotten

        return elapsed if not fresh else -1
