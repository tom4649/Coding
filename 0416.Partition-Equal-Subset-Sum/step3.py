class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        can_partition = [False] * (total // 2 + 1)
        can_partition[0] = True

        for num in nums:
            for value in range(len(can_partition) - num - 1, -1, -1):
                if can_partition[value]:
                    can_partition[value + num] = True

        return can_partition[-1]
