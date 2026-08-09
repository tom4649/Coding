class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        expected = 0
        for i in range(len(sorted_nums)):
            if sorted_nums[i] != expected:
                break
            expected += 1

        return expected
