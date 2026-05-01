import itertools
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        prefix_sums = itertools.accumulate(nums)
        num_subarray = 0
        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[k] += 1
        for prefix_sum in prefix_sums:
            num_subarray += prefix_sum_to_count[prefix_sum]
            prefix_sum_to_count[k + prefix_sum] += 1
        return num_subarray
