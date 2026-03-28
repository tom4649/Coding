class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        max_nums = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            max_nums.append(max(max_nums[i - 2], max_nums[i - 1] + nums[i]))

        return max_nums[-1]
