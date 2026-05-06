import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_subarray_len = float("inf")
        for right, num_right in enumerate(nums):
            current_sum += num_right
            if current_sum < target:
                continue
            while left < len(nums) and current_sum - nums[left] >= target:
                current_sum -= nums[left]
                left += 1
            min_subarray_len = min(min_subarray_len, right - left + 1)

        return 0 if math.isinf(min_subarray_len) else min_subarray_len
