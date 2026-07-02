class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        subsets = []

        subset = []
        def update_subsets(i):
            if i == len(nums):
                subsets.append(subset[:])
                return

            subset.append(nums[i])
            update_subsets(i+1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            update_subsets(i+1)

        update_subsets(0)

        return subsets


