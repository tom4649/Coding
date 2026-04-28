"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        end_times = []
        intervals = sorted(intervals, key=lambda x: x.start)
        for interval in intervals:
            if end_times and end_times[0] < interval.start:
                heapq.heappop(end_times)
            heapq.heappush(end_times, interval.end)
        return len(end_times)
