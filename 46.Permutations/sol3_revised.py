class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        frontier = [([], (1 << n) - 1)]

        while frontier:
            fixed, mask = frontier.pop()
            if len(fixed) == n:
                permutations.append(fixed)
                continue
            m = mask
            while m:
                lsb = m & -m
                i = lsb.bit_length() - 1
                m ^= lsb
                frontier.append((fixed + [nums[i]], mask ^ lsb))

        return permutations
