import bisect
import functools


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        jobs_sorted_by_start = sorted((t, i) for i, t in enumerate(startTime))
        sorted_to_original_index = {
            job_index: original_index
            for job_index, (_, original_index) in enumerate(jobs_sorted_by_start)
        }

        @functools.cache
        def max_profit_after(job_index: int):
            if job_index >= len(startTime):
                return 0

            original_index = sorted_to_original_index[job_index]
            next_job_index = bisect.bisect_left(
                jobs_sorted_by_start, (endTime[original_index], -1)
            )

            return max(
                max_profit_after(job_index + 1),
                profit[original_index] + max_profit_after(next_job_index),
            )

        return max_profit_after(0)
