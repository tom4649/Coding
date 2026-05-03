from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for i, num in enumerate(nums):
            pos_insert = bisect_left(tails, num)
            if pos_insert == len(tails):
                tails.append(num)
            else:
                tails[pos_insert] = num

        return len(tails)
