class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def skip_nonzeros(index):
            while index < len(nums) and nums[index] != 0:
                index += 1
            return index

        def skip_zeros(index):
            while index < len(nums) and nums[index] == 0:
                index += 1
            return index

        scanning_index = 0
        while scanning_index < len(nums):
            first_zero_index = skip_nonzeros(scanning_index)
            scanning_index = skip_zeros(first_zero_index)
            if scanning_index == len(nums):
                return
            while nums[first_zero_index] == 0 and scanning_index < len(nums):
                nums[scanning_index], nums[first_zero_index] = (
                    nums[first_zero_index],
                    nums[scanning_index],
                )
                scanning_index = skip_zeros(scanning_index)
                first_zero_index += 1

        return
