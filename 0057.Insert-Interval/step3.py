import bisect
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]

        new_start, new_end = newInterval
        merge_start = bisect.bisect_left(ends, new_start)
        merge_end = bisect.bisect_right(starts, new_end)

        if merge_start < merge_end:
            new_start = min(new_start, starts[merge_start])
            new_end = max(new_end, ends[merge_end - 1])

        return intervals[:merge_start] + [[new_start, new_end]] + intervals[merge_end:]


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        index = 0
        new_start, new_end = newInterval

        earlier_intervals = []
        while index < len(intervals) and intervals[index][1] < new_start:
            earlier_intervals.append(intervals[index])
            index += 1

        while index < len(intervals) and intervals[index][0] <= new_end:
            new_start = min(new_start, intervals[index][0])
            new_end = max(new_end, intervals[index][1])
            index += 1

        return earlier_intervals + [[new_start, new_end]] + intervals[index:]
