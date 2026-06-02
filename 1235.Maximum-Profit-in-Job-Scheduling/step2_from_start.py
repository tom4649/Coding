class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        time_to_index = {
            t: i for i, t in enumerate(sorted(set(startTime) | set(endTime)))
        }
        jobs_sorted_by_end = sorted(
            (time_to_index[end], i) for i, end in enumerate(endTime)
        )

        # dp[t]: the maximum profit up to time t
        dp = [0] * len(time_to_index)
        end_previous = 0

        for end, original_index in jobs_sorted_by_end:
            for t in range(end_previous + 1, end):
                dp[t] = dp[end_previous]

            start = time_to_index[startTime[original_index]]

            dp[end] = max(dp[end_previous], dp[start] + profit[original_index])
            end_previous = end

        return dp[end_previous]
