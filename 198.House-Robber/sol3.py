from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("The input list is empty")

        @cache
        def rob_helper(idx):
            if idx < 2:
                return max(nums[: idx + 1])

            return max(rob_helper(idx - 1), rob_helper(idx - 2) + nums[idx])

        return rob_helper(len(nums) - 1)
