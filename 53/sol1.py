class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        cummulative_sum = 0
        min_cummulative_sum = 0
        for n in nums:
            cummulative_sum += n
            max_sum = max(max_sum, cummulative_sum - min_cummulative_sum)
            min_cummulative_sum = min(min_cummulative_sum, cummulative_sum)

        return max_sum
