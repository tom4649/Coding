class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        fixed = []
        not_used = set(nums)

        def traverse():
            if len(fixed) == len(nums):
                permutations.append(fixed.copy())
                return
            for num in list(not_used):
                not_used.remove(num)
                fixed.append(num)
                traverse()
                fixed.pop()
                not_used.add(num)

        traverse()
        return permutations
