import collections

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        num_to_count = collections.Counter(nums)
        subsets = [[]]
        for n, count in num_to_count.items():
            subsets.extend([subset + [n] * i for i in range(1, count + 1) for subset in subsets])
        return subsets
