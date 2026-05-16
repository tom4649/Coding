class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        ways = 1
        ways_previous = 1

        for _ in range(n - 1):
            ways, ways_previous = ways + ways_previous, ways

        return ways


class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(step: int) -> tuple[int, int]:
            if step == 1:
                return 1, 1
            ways_prev_step, ways_two_steps_back = helper(step - 1)
            return ways_prev_step + ways_two_steps_back, ways_prev_step

        return helper(n)[0]
