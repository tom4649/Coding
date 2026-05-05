import bisect


class Solution:
    def findMin(self, nums: List[int]) -> int:
        index = bisect.bisect_left(nums, True, key=lambda x: x < nums[0])
        return nums[index % len(nums)]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        index = bisect.bisect_left(nums, True, key=lambda x: x <= nums[-1])
        return nums[index]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        index = bisect.bisect_right(nums, False, key=lambda x: x < nums[0])
        return nums[index % len(nums)]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        index = bisect.bisect_right(nums, False, key=lambda x: x <= nums[-1])
        return nums[index]
