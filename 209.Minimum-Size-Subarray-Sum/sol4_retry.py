import bisect
import itertools
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        prefix_sum = list(itertools.accumulate(nums, initial=0))
        n = len(nums)
        min_subarray_len = float("inf")
        for left, prev_sum in enumerate(prefix_sum):
            right = bisect.bisect_left(prefix_sum, prev_sum + target, lo=left + 1)
            if right <= n:
                min_subarray_len = min(min_subarray_len, right - left)
        return 0 if math.isinf(min_subarray_len) else min_subarray_len
