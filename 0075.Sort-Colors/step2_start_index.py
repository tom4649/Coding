class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_start = 0  # i < zero_start -> nums[i] == 0
        one_start = 0  # i < one_start and i >= zero_start -> nums[i] == 0

        for two_start in range(len(nums)):
            if nums[two_start] == 0:
                nums[two_start], nums[zero_start] = nums[zero_start], nums[two_start]
                zero_start += 1
                one_start = max(zero_start, one_start)
            if nums[two_start] == 1:
                nums[two_start], nums[one_start] = nums[one_start], nums[two_start]
                one_start += 1
