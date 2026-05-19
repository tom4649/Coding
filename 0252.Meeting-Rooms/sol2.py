"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import sched


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        all_times = set()
        for interval in intervals:
            all_times.add(interval.start)
            all_times.add(interval.end)
        all_times_list = sorted(list(all_times))

        time_to_rank = {}
        for rank, time in enumerate(all_times_list):
            time_to_rank[time] = rank
        schedules = [0] * len(all_times_list)

        for interval in intervals:
            schedules[time_to_rank[interval.start]] += 1
            schedules[time_to_rank[interval.end]] -= 1

        prefix_sum = 0
        for schedule in schedules:
            prefix_sum += schedule
            if prefix_sum >= 2:
                return False
        return True
