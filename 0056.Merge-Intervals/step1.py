import itertools


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        unique_times = sorted(list(set(t for interval in intervals for t in interval)))
        time_to_rank = {t: i for i, t in enumerate(unique_times)}
        rank_to_time = {i: t for i, t in enumerate(unique_times)}

        time_counts = [0] * len(unique_times)
        point_intervals = []
        for start, end in intervals:
            time_counts[time_to_rank[start]] += 1
            time_counts[time_to_rank[end]] -= 1
            if start == end:
                point_intervals.append(start)

        prefix_sum = list(itertools.accumulate(time_counts))
        print(prefix_sum)
        result = []
        i = 0
        while i < len(prefix_sum):
            if prefix_sum[i] == 0:
                i += 1
                continue
            start = rank_to_time[i]
            while prefix_sum[i] != 0:
                i += 1
            result.append([start, rank_to_time[i]])
            i += 1
        for t in point_intervals:
            if (
                prefix_sum[time_to_rank[t]] == 0
                and prefix_sum[time_to_rank[t] - 1] == 0
            ):
                result.append([t, t])

        return result
