from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = []
        prefix_sum = 0
        for value in nums:
            prefix_sum += value
            prefix_sums.append(prefix_sum)

        answer = 0
        prefix_sums.reverse()
        prefix_sums.append(0)

        needed_prefix_sum_counts = defaultdict(int)
        for prefix_sum in prefix_sums:
            answer += needed_prefix_sum_counts[prefix_sum]
            needed_prefix_sum = prefix_sum - k
            needed_prefix_sum_counts[needed_prefix_sum] += 1
        return answer
