import bisect


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        jobs_sorted_by_start = sorted((t, i) for i, t in enumerate(startTime))

        # dp[index_job]: the maximum profit taking elements from the suffix starting at index_job
        dp = [0] * len(startTime)

        for index_reversed, (start, index_job) in enumerate(
            reversed(jobs_sorted_by_start)
        ):
            index_dp = len(startTime) - 1 - index_reversed

            if index_reversed == 0:
                dp[index_dp] = profit[index_job]
                continue

            end = endTime[index_job]

            index_next_job = bisect.bisect_left(jobs_sorted_by_start, (end, -1))

            if index_next_job >= len(startTime):
                dp[index_dp] = max(dp[index_dp + 1], profit[index_job])
                continue

            dp[index_dp] = max(dp[index_dp + 1], profit[index_job] + dp[index_next_job])

        return dp[0]
