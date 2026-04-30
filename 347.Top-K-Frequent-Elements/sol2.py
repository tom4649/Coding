from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_counts = defaultdict(int)
        for num in nums:
            num_to_counts[num] += 1
        num_to_counts_sorted = list(sorted(num_to_counts.items(), key=lambda x: -x[1]))
        return list(map(lambda x: x[0], num_to_counts_sorted[:k]))



