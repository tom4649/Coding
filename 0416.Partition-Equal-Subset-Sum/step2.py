class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        # reachable[s]: whether some subset of nums seen so far sums to s
        reachable = [False] * (target + 1)
        reachable[0] = True

        for num in nums:
            for s in range(target - num, -1, -1):
                if reachable[s]:
                    reachable[s + num] = True
                    if s + num == target:
                        return True

        return reachable[target]
