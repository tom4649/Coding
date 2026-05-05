class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_len = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[non_zero_len] = (
                    nums[non_zero_len],
                    nums[index],
                )
                non_zero_len += 1

        return
