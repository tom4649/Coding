class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        scannning_index = 0
        while scannning_index < len(nums):
            while scannning_index < len(nums) and nums[scannning_index] != 0:
                scannning_index += 1
            if scannning_index == len(nums):
                return
            first_zero_index = scannning_index
            while scannning_index < len(nums) and nums[scannning_index] == 0:
                scannning_index += 1
            if scannning_index == len(nums):
                return
            while nums[first_zero_index] == 0 and scannning_index < len(nums):
                nums[scannning_index], nums[first_zero_index] = (
                    nums[first_zero_index],
                    nums[scannning_index],
                )
                while scannning_index < len(nums) and nums[scannning_index] == 0:
                    scannning_index += 1
                first_zero_index += 1

        return
