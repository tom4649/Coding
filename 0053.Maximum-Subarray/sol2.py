class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -float("inf")
        max_ending_with_n = -float("inf")
        for n in nums:
            max_ending_with_n = max(n, max_ending_with_n + n)
            max_so_far = max(max_so_far, max_ending_with_n)

        return max_so_far
