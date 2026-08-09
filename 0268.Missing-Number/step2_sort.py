class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        expected = 0
        for expected, actual in enumerate(sorted_nums):
            if expected != actual:
                return expected

        return len(nums)
