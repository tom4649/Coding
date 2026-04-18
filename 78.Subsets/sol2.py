class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        frontier = [([], -1)]

        while frontier:
            fixed, determined_idx = frontier.pop()
            if determined_idx == len(nums) - 1:
                subsets.append(fixed)
                continue
            frontier.append((fixed, determined_idx + 1))
            frontier.append((fixed + [nums[determined_idx + 1]], determined_idx + 1))

        return subsets
