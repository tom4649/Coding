from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)

        prefix_sum = 0
        count = 0
        for n in nums:
            prefix_count[prefix_sum] += 1
            prefix_sum += n
            count += prefix_count[prefix_sum - k]
        return count
