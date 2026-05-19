from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i] is the smallest ending element of all increasing subsequences of length (i + 1)
        tails = []
        for n in nums:
            pos_insert_n = bisect_left(tails, n)
            if pos_insert_n >= len(tails):
                tails.append(n)
                continue
            tails[pos_insert_n] = n

        return len(tails)
