from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1
        sorted_nums, _ = zip(
            *sorted(num_to_count.items(), key=lambda x: x[1], reversed=True)
        )
        return sorted_nums[:k]
