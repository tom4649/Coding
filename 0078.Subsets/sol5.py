import itertools


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = [[]]
        for value in nums:
            a, b = itertools.tee(results)
            results = itertools.chain(a, map(lambda s, v=value: s + [v], b))
        return list(results)
