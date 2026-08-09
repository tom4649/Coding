import collections

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        num_to_count = collections.defaultdict(int)
        for n in nums:
            num_to_count[n] += 1

        subsets = [[]]
        for n, count in num_to_count.items():
            extention = []
            for i in range(1, count + 1):
                extention.extend([subset + [n] * i for subset in subsets])
            subsets.extend(extention)

        return subsets
