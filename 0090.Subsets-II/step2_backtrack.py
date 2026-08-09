class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        def update_subsets(subsets, i, subset):
            if i == len(nums):
                subsets.append(subset[:])
                return

            subset.append(nums[i])
            update_subsets(subsets, i+1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            update_subsets(subsets, i+1, subset)

        subsets = []
        update_subsets(subsets, 0, [])

        return subsets


