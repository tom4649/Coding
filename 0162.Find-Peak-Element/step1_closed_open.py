class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if mid < len(nums) and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
