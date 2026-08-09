import bisect


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        def is_decreasing(index):
            return index == len(nums) - 1 or nums[index] > nums[index + 1]

        return bisect.bisect_left(range(len(nums)), True, key=is_decreasing)
