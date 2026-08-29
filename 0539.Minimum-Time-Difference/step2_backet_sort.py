class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        MINUTES_IN_DAY = 24 * 60

        if len(timePoints) > MINUTES_IN_DAY:
            return 0

        def time_to_minutes(time_point: str) -> int:
            hours, minutes = time_point.split(":")
            return int(hours) * 60 + int(minutes)

        seen = [False] * MINUTES_IN_DAY
        for time_point in timePoints:
            time_in_minutes = time_to_minutes(time_point)
            if seen[time_in_minutes]:
                return 0
            seen[time_in_minutes] = True

        min_difference = float("inf")
        previous_time = None
        first_time = None
        last_time = None
        for time_in_minutes in range(len(seen)):
            if not seen[time_in_minutes]:
                continue

            if first_time is None:
                first_time = time_in_minutes
                previous_time = time_in_minutes
                continue

            min_difference = min(min_difference, time_in_minutes - previous_time)
            previous_time = time_in_minutes
            last_time = time_in_minutes

        min_difference = min(min_difference, first_time - last_time + MINUTES_IN_DAY)

        return min_difference
