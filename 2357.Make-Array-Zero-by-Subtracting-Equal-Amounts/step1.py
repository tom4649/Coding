class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)

        len_zero = 0
        while len_zero < len(sorted_nums) and sorted_nums[len_zero] == 0:
            len_zero += 1

        if len_zero == len(sorted_nums):
            return 0

        subtracted = 0
        num_operation = 0

        while subtracted < sorted_nums[-1]:
            subtracted = sorted_nums[len_zero]
            num_operation += 1
            while len_zero < len(sorted_nums) and sorted_nums[len_zero] <= subtracted:
                len_zero += 1

        return num_operation
