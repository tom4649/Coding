class Solution:
    def rob_linearly(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) < 3:
            return max(nums)

        max_with_last = nums[1]
        max_with_out_last = nums[0]
        for n in nums[2:]:
            max_with_last, max_with_out_last = (
                max(max_with_out_last + n, max_with_last),
                max(max_with_last, max_with_out_last),
            )
        return max_with_last

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        return max(self.rob_linearly(nums[:-1]), self.rob_linearly(nums[1:]))
