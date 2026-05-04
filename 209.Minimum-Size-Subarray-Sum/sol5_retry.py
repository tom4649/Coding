import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_subarray_len = float("inf")
        for right, n in enumerate(nums):
            total += n
            if total < target:
                continue
            while left < len(nums) - 1 and total - nums[left] >= target:
                total -= nums[left]
                left += 1
            min_subarray_len = min(min_subarray_len, right - left + 1)
        return min_subarray_len if not math.isinf(min_subarray_len) else 0
