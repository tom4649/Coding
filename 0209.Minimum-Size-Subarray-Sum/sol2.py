import itertools
import bisect
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_subarray_len = float("inf")
        prefix_sum = list(itertools.accumulate(nums))
        for left, num_left in enumerate(nums):
            right = bisect.bisect_left(prefix_sum, target + prefix_sum[left] - num_left)
            if right < len(nums):
                min_subarray_len = min(min_subarray_len, right - left + 1)
        return 0 if math.isinf(min_subarray_len) else min_subarray_len
