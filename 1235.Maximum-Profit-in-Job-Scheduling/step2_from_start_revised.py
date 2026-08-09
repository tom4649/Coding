from dataclasses import dataclass


@dataclass
class Job:
    start: int
    end: int
    profit: int


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        time_to_index = {
            t: i for i, t in enumerate(sorted(set(startTime) | set(endTime)))
        }

        jobs = [
            Job(time_to_index[startTime[i]], time_to_index[endTime[i]], profit[i])
            for i in range(len(startTime))
        ]
        jobs.sort(key=lambda j: j.end)

        # dp[t]: the maximum profit up to time t
        dp = [0] * len(time_to_index)
        i = 0
        for job in jobs:
            while i < job.end:
                dp[i + 1] = dp[i]
                i += 1

            dp[job.end] = max(dp[job.end], dp[job.start] + job.profit)

        return dp[-1]
