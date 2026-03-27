class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        max_sum_end_with_current_n = -float("inf")
        for n in nums:
            max_sum_end_with_current_n = max(max_sum_end_with_current_n + n, n)
            max_sum = max(max_sum, max_sum_end_with_current_n)

        return max_sum
