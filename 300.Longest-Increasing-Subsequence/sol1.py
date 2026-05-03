class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # len_is[i] is Length of increasing subsequence which ends with nums[i]
        len_is = [1] * len(nums)
        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    len_is[i] = max(
                        len_is[i],
                        len_is[j] + 1,
                    )

        return max(len_is)
