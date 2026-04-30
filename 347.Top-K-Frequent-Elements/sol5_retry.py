from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_nums, _ = zip(*counter.most_common())
        print(type(sorted_nums))
        return sorted_nums[:k]
