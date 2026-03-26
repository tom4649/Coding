class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length_of_is = [1] * len(nums)
        for i, n in enumerate(nums):
            for j in range(i):
                if n > nums[j]:
                    length_of_is[i] = max(length_of_is[i], length_of_is[j] + 1)

        return max(length_of_is)
