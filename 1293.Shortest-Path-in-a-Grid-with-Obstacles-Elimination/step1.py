EMPTY = 0
OBSTACLE = 1

class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return -1

        num_rows = len(grid)
        num_cols = len(grid[0])

        max_remaining_k = [[-1] * num_cols for _ in range(num_rows)]
        max_remaining_k[0][0] = k

        frontier = [(0, 0, k)]
        steps = 0

        while frontier:
            next_frontier = []
            for row, col, remaining_k in frontier:
                if row == num_rows - 1 and col == num_cols - 1:
                    return steps

                for next_row, next_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    if not (0 <= next_row < num_rows and 0 <= next_col < num_cols):
                        continue

                    is_obstacle = (grid[next_row][next_col] == OBSTACLE)
                    next_remaining_k = remaining_k - (1 if is_obstacle else 0)

                    if next_remaining_k < 0:
                        continue

                    if max_remaining_k[next_row][next_col] >= next_remaining_k:
                        continue

                    max_remaining_k[next_row][next_col] = next_remaining_k
                    next_frontier.append((next_row, next_col, next_remaining_k))

            frontier = next_frontier
            steps += 1

        return -1
