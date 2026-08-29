class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time_point: str):
            hours, minutes = time_point.split(":")
            return 60 * int(hours) + int(minutes)

        minutes = [time_to_minutes(time_point) for time_point in timePoints]
        minutes.sort()
        minutes.append(minutes[0] + 24 * 60)

        min_difference = float("inf")
        for i in range(len(minutes) - 1):
            min_difference = min(min_difference, minutes[i+1] - minutes[i])

        return min_difference


