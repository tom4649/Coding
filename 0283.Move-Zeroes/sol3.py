class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_index = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[last_non_zero_index] = (
                    nums[last_non_zero_index],
                    nums[index],
                )
                last_non_zero_index += 1

        return
