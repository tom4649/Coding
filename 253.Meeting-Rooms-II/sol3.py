"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        used_rooms = 0
        min_meeting_rooms = 0
        end_index = 0

        for start in starts:
            if start >= ends[end_index]:
                used_rooms -= 1
                end_index += 1

            used_rooms += 1
            min_meeting_rooms = max(min_meeting_rooms, used_rooms)

        return min_meeting_rooms
