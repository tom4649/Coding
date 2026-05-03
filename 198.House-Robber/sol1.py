class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("The input list is empty")

        if len(nums) < 2:
            return max(nums)

        max_nums = [nums[0], max(nums[0], nums[1])] + [0] * (len(nums) - 2)

        for i in range(2, len(nums)):
            max_nums[i] = max(max_nums[i - 1], max_nums[i - 2] + nums[i])

        return max_nums[-1]
