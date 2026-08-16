class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        MINUTES_IN_DAY = 24 * 60

        def time_to_minutes(time_point: str) -> int:
            hours, minutes = time_point.split(":")
            return int(hours) * 60 + int(minutes)

        times_in_minutes = sorted(time_to_minutes(time_point) for time_point in timePoints)
        times_in_minutes.append(times_in_minutes[0] + MINUTES_IN_DAY)

        min_difference = float("inf")
        for i in range(len(times_in_minutes) - 1):
            min_difference = min(min_difference, times_in_minutes[i+1] - times_in_minutes[i])

        return min_difference
