import bisect


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        start_and_index = sorted((t, i) for i, t in enumerate(startTime))
        dp = [0] * len(startTime)

        for i, (start, index) in enumerate(reversed(start_and_index)):
            if i == 0:
                dp[-i - 1] = profit[index]
                continue
            end = endTime[index]
            i_after = bisect.bisect_left(start_and_index, (end, -1))
            if i_after >= len(start_and_index):
                dp[-i - 1] = max(dp[-i], profit[index])
                continue
            dp[-i - 1] = max(dp[-i], profit[index] + dp[i_after])

        return dp[0]
