import bisect

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        left_index = bisect.bisect_left(nums, target)
        right_index = bisect.bisect_right(nums, target)

        if left_index >= len(nums) or nums[left_index] != target:
            return [-1, -1]

        return [left_index, right_index - 1]


