class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []

        def build_subset_after_index(index: int):
            if index == len(nums):
                subsets.append(subset.copy())
                return
            subset.append(nums[index])
            build_subset_after_index(index + 1)
            subset.pop()
            build_subset_after_index(index + 1)

        build_subset_after_index(0)

        return subsets
