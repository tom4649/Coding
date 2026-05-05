from enum import Enum, auto


class SkipMode(Enum):
    SKIP_NONZEROS = auto()
    SKIP_ZEROS = auto()


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def skip_index(index, mode: SkipMode) -> int:
            if mode is SkipMode.SKIP_NONZEROS:
                while index < len(nums) and nums[index] != 0:
                    index += 1
            elif mode is SkipMode.SKIP_ZEROS:
                while index < len(nums) and nums[index] == 0:
                    index += 1
            return index

        scanning_index = 0
        while scanning_index < len(nums):
            first_zero_index = skip_index(scanning_index, SkipMode.SKIP_NONZEROS)
            scanning_index = skip_index(first_zero_index, SkipMode.SKIP_ZEROS)
            if scanning_index == len(nums):
                return
            while nums[first_zero_index] == 0 and scanning_index < len(nums):
                nums[scanning_index], nums[first_zero_index] = (
                    nums[first_zero_index],
                    nums[scanning_index],
                )
                scanning_index = skip_index(scanning_index, SkipMode.SKIP_ZEROS)
                first_zero_index += 1

        return
