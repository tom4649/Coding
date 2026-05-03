class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        cumulative_sum = 0
        min_cumulative_sum = 0
        for n in nums:
            cumulative_sum += n
            max_sum = max(max_sum, cumulative_sum - min_cumulative_sum)
            min_cumulative_sum = min(min_cumulative_sum, cumulative_sum)

        return max_sum
