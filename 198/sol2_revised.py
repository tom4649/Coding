class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("The input list is empty")

        if len(nums) < 2:
            return max(nums)

        # max_with_last: after each iteration, best total for houses 0..i for each i.
        # max_without_last: at loop start, best total for houses 0..i-1 for each i.
        max_with_last = nums[0]
        max_without_last = 0

        for i in range(1, len(nums)):
            next_max_without_last = max_with_last
            max_with_last = max(max_with_last, max_without_last + nums[i])
            max_without_last = next_max_without_last

        return max_with_last
