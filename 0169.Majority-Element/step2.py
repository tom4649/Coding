import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        most_common = counter.most_common(1)[0]
        return most_common[0] if most_common[1] > len(nums) // 2 else -1


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
