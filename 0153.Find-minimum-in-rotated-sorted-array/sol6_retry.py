class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > nums[-1]:
                left = middle + 1
            else:
                right = middle
        return nums[left]
