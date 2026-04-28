"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time_and_change = []
        for interval in intervals:
            time_and_change.append((interval.start, 1))
            time_and_change.append((interval.end, -1))
        time_and_change.sort()

        min_meeting_rooms = 0
        current_rooms = 0
        for _, change in time_and_change:
            current_rooms += change
            min_meeting_rooms = max(min_meeting_rooms, current_rooms)

        return min_meeting_rooms
