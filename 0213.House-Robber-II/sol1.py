class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        def rob_without_circle(nums_without_circle):
            max_with_last = nums_without_circle[0]
            max_without_last = 0

            for i in range(1, len(nums_without_circle)):
                next_max_without_last = max_with_last
                max_with_last = max(
                    max_with_last, max_without_last + nums_without_circle[i]
                )
                max_without_last = next_max_without_last

            return max(max_with_last, max_without_last)

        max_value_without_first = rob_without_circle(nums[1:])
        max_value_without_last = rob_without_circle(nums[:-1])
        return max(max_value_without_first, max_value_without_last)
