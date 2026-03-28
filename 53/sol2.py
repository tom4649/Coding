class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        max_ending_here = -float("inf")
        for n in nums:
            max_ending_here = max(n, max_ending_here + n)
            max_so_far = max(max_so_far, max_ending_here)

        return max_sum
