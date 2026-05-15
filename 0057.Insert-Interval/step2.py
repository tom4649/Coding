import bisect
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        new_start, new_end = newInterval

        index = 0
        while index < len(intervals) and intervals[index][1] < new_start:
            result.append(intervals[index])
            index += 1

        while index < len(intervals) and intervals[index][0] <= new_end:
            new_start = min(new_start, intervals[index][0])
            new_end = max(new_end, intervals[index][1])
            index += 1

        result.append([new_start, new_end])
        result.extend(intervals[index:])
        return result


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        starts = [start for start, _ in intervals]
        ends = [end for _, end in intervals]
        new_start, new_end = newInterval

        merge_start = bisect.bisect_left(ends, new_start)
        merge_end = bisect.bisect_right(starts, new_end)

        if merge_start < merge_end:
            new_start = min(new_start, intervals[merge_start][0])
            new_end = max(new_end, intervals[merge_end - 1][1])

        return intervals[:merge_start] + [[new_start, new_end]] + intervals[merge_end:]


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        sorted_intervals = sorted(intervals + [newInterval])

        merged = []
        for start, end in sorted_intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged
