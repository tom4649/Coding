import functools


class Solution:
    def climbStairs(self, n: int) -> int:
        @functools.cache
        def climb_stairs_helper(n):
            if n == 0 or n == 1:
                return 1

            return climb_stairs_helper(n - 1) + climb_stairs_helper(n - 2)

        return climb_stairs_helper(n)
