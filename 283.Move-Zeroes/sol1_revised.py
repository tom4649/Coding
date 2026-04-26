class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        scanning_index = 0
        while scanning_index < len(nums):
            while scanning_index < len(nums):
                if nums[scanning_index] == 0:
                    break
                scanning_index += 1
            if scanning_index == len(nums):
                return

            first_zero_index = scanning_index
            while scanning_index < len(nums):
                if nums[scanning_index] != 0:
                    break
                scanning_index += 1
            if scanning_index == len(nums):
                return

            while nums[first_zero_index] == 0 and scanning_index < len(nums):
                nums[scanning_index], nums[first_zero_index] = (
                    nums[first_zero_index],
                    nums[scanning_index],
                )
                while scanning_index < len(nums):
                    if nums[scanning_index] != 0:
                        break
                    scanning_index += 1
                first_zero_index += 1

        return
