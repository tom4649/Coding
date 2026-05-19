class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        frontier = [([], set(nums))]

        while frontier:
            fixed, not_used = frontier.pop()
            if len(fixed) == len(nums):
                permutations.append(fixed)
                continue
            for num in not_used:
                frontier.append((fixed + [num], not_used - {num}))

        return permutations
