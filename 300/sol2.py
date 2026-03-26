from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for n in nums:
            lis_if_tail_is_n = bisect_left(tails, n) + 1
            if lis_if_tail_is_n > len(tails):
                tails.append(n)
                continue
            tails[lis_if_tail_is_n - 1] = n

        return len(tails)
