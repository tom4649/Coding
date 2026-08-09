import itertools


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_points = sorted({point for interval in intervals for point in interval})
        point_to_index = {point: i for i, point in enumerate(sorted_points)}

        deltas = [0] * len(sorted_points)
        zero_length_intervals = []
        for start, end in intervals:
            deltas[point_to_index[start]] += 1
            deltas[point_to_index[end]] -= 1
            if start == end:
                zero_length_intervals.append(start)

        active_counts = list(itertools.accumulate(deltas))
        merged = []
        index = 0
        while index < len(active_counts):
            if active_counts[index] == 0:
                index += 1
                continue
            start = sorted_points[index]
            while active_counts[index] != 0:
                index += 1
            merged.append([start, sorted_points[index]])
            index += 1

        for point in zero_length_intervals:
            point_index = point_to_index[point]
            if active_counts[point_index] == 0 and active_counts[point_index - 1] == 0:
                merged.append([point, point])

        return merged
