import collections

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def update_subsets(subsets, num, count):
            subsets.extend([subset + [num] * i for i in range(1, count + 1) for subset in subsets[:]])


        num_to_count = collections.Counter(nums)
        subsets = [[]]
        for num, count in num_to_count.items():
            update_subsets(subsets, num, count)

        return subsets


