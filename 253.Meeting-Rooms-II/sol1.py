"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        all_times = set()
        for interval in intervals:
            all_times.add(interval.start)
            all_times.add(interval.end)
        all_times_list = sorted(list(all_times))
        time_to_rank = {}
        for rank, time in enumerate(all_times_list):
            time_to_rank[time] = rank
        all_schedules = [0] * len(all_times_list)
        for interval in intervals:
            all_schedules[time_to_rank[interval.start]] += 1
            all_schedules[time_to_rank[interval.end]] -= 1
        prefix_sum = 0
        min_meeting_rooms = 0
        for schedule in all_schedules:
            prefix_sum += schedule
            min_meeting_rooms = max(min_meeting_rooms, prefix_sum)
        return min_meeting_rooms
