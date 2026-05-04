class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for value in nums:
            subsets.extend([subset + [value] for subset in subsets])

        return subsets
