class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("The input list is empty.")
        left = 0
        right = len(nums)
        pivot = nums[0]

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= pivot:
                left = mid + 1
            else:
                right = mid

        return nums[left] if left < len(nums) else pivot
