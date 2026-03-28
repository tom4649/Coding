import functools
import itertools


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        def rob_linearly(sequence):
            def visit_next(state, money):
                max_with_last, max_without_last = state
                next_max_without_last = max_with_last
                max_with_last = max(max_with_last, max_without_last + money)
                return max_with_last, next_max_without_last

            return max(functools.reduce(visit_next, sequence, (0, 0)))

        return max(
            rob_linearly(itertools.islice(nums, 0, len(nums) - 1)),
            rob_linearly(itertools.islice(nums, 1, len(nums))),
        )
