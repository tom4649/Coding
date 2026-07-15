class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        for actual in nums:
            xor_sum ^= actual
        for expected in range(len(nums)+1):
            xor_sum ^= expected

        return xor_sum
