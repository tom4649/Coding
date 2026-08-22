import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        if len(grid) != len(grid[0]):
            raise ValueError("invalid grid")

        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        costs = [n * n] * (n * n)
        costs[0] = grid[0][0]

        while heap:
            cost, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return cost

            for r_next, c_next in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= r_next < n and 0 <= c_next < n):
                    continue
                cost_next = max(cost, grid[r_next][c_next])
                if cost_next < costs[r_next * n + c_next]:
                    costs[r_next * n + c_next] = cost_next
                    heapq.heappush(heap, (cost_next, r_next, c_next))

