class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target: # i < left -> nums[i] < target
                left = middle + 1
            else:
                right = middle # i >= right -> nums[i] >= target
        idx_left =  left

        if idx_left >= len(nums) or nums[idx_left] != target:
            return [-1, -1]

        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] <= target: # i < left -> nums[i] <= target
                left = middle + 1
            else:
                right = middle # i >= right -> nums[i] > target
        idx_right =  left

        return [idx_left, idx_right - 1]


