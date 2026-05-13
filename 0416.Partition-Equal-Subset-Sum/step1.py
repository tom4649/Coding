class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        sorted_nums = sorted(nums)
        possible_sum = [False] * (total // 2 + 1)
        possible_sum[0] = True
        possible_sum_prev = possible_sum[:]

        for num in sorted_nums:
            for i in range(len(possible_sum) - num):
                if possible_sum_prev[i]:
                    possible_sum[i + num] = True
            possible_sum_prev = possible_sum[:]

        return possible_sum[-1]
