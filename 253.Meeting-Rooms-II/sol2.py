"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        unique_times = set()
        for interval in intervals:
            unique_times.add(interval.start)
            unique_times.add(interval.end)

        sorted_times = sorted(list(unique_times))

        time_to_rank = {}
        for rank, time in enumerate(sorted_times):
            time_to_rank[time] = rank

        timeline = [0] * len(sorted_times)
        for interval in intervals:
            timeline[time_to_rank[interval.start]] += 1
            timeline[time_to_rank[interval.end]] -= 1

        current_rooms = 0
        min_meeting_rooms = 0
        for change in timeline:
            current_rooms += change
            min_meeting_rooms = max(min_meeting_rooms, current_rooms)

        return min_meeting_rooms
