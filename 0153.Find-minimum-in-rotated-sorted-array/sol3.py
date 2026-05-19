class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("The input list is empty.")
        pivot = nums[-1]
        right = len(nums) - 1  # i >= right -> nums[i] <= pivot
        left = 0  # i < left -> nums[i] > pivot

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= pivot:
                left = mid + 1
            else:
                right = mid

        return nums[right]
