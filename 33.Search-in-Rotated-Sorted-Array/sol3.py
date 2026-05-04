import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        len_nums = len(nums)

        def comp(a, b):
            return (a < b) - (a > b)

        def priority(x):
            return (x > nums[-1]) * -2 + comp(target, x)

        possible_index = bisect.bisect_left(nums, priority(target), key=priority)
        return possible_index if nums[possible_index] == target else -1
