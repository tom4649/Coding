class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_cumulative_sum_so_far = 0
        cumulative_sum = 0
        total_max_subarray = -float("inf")
        for n in nums:
            cumulative_sum += n
            total_max_subarray = max(
                cumulative_sum - min_cumulative_sum_so_far, total_max_subarray
            )
            min_cumulative_sum_so_far = min(min_cumulative_sum_so_far, cumulative_sum)
        return total_max_subarray
