class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        mask = (1 << len(nums)) - 1
        while mask >= 0:
            subsets.append([num for i, num in enumerate(nums) if (mask >> i) & 1])
            mask -= 1
        return subsets
