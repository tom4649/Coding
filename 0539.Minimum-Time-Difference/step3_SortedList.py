from sortedcontainers import SortedList

class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        MINUTES_IN_DAY = 24 * 60

        if len(timePoints) > MINUTES_IN_DAY:
            return 0

        def time_to_minutes(time_point: str) -> int:
            h, m = time_point.split(":")
            return int(h) * 60 + int(m)

        sorted_time_points = SortedList()
        min_difference = float("inf")

        for tp in timePoints:
            time_in_minutes = time_to_minutes(tp)
            if time_in_minutes in sorted_time_points:
                return 0

            index = sorted_time_points.bisect_left(time_in_minutes)

            if index < len(sorted_time_points):
                min_difference = min(min_difference, sorted_time_points[index] - time_in_minutes)
            elif sorted_time_points:
                min_difference = min(min_difference, sorted_time_points[0] + 1440 - time_in_minutes)

            if index > 0:
                min_difference = min(min_difference, time_in_minutes - sorted_time_points[index - 1])
            elif sorted_time_points:
                min_difference = min(min_difference, time_in_minutes + 1440 - sorted_time_points[-1])

            sorted_time_points.add(time_in_minutes)

        return min_difference
