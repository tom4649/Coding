class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        if len(grid) != len(grid[0]):
            raise ValueError("invalid grid")

        n = len(grid)

        def can_reach_within(t):
            if grid[0][0] > t:
                return False

            reachable = [(0, 0)]
            seen = set((0, 0))
            while reachable:
                next_reachable = []
                for r, c in reachable:
                    if r == n - 1 and c == n - 1:
                        return True
                    for r_next, c_next in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if not (0 <= r_next < n and 0 <= c_next < n):
                            continue
                        if (r_next, c_next) in seen or grid[r_next][c_next] > t:
                            continue
                        seen.add((r_next, c_next))
                        next_reachable.append((r_next, c_next))
                reachable = next_reachable

            return False


        left = 0
        right = n * n
        while left < right:
            mid = (left + right) // 2
            if not can_reach_within(mid):
                left = mid + 1
            else:
                right = mid

        return left


