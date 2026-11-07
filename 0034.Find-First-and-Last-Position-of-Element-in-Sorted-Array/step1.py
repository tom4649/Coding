import bisect

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        idx_left = bisect.bisect_left(nums, target)
        idx_right = bisect.bisect_right(nums, target)

        if idx_left >= len(nums) or nums[idx_left] != target:
            return [-1, -1]

        return [idx_left, idx_right - 1]


