from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_to_count = {}
        for n in nums:
            num_to_count[n] = num_to_count.setdefault(n, 0) + 1
            if num_to_count[n] > len(nums) // 2:
                return n
        return -1
