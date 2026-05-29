import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = collections.Counter(tasks)
        least_commons = counter.most_common()[::-1]
        least_counts = [common[1] for common in least_commons]

        num_intervals = 0

        while least_counts:
            loop_size = n + 1
            num_loop = min(loop_size, len(least_counts))
            indices_loop = list(
                range(len(least_counts) - 1, len(least_counts) - 1 - num_loop, -1)
            )
            for i in indices_loop:
                least_counts[i] -= 1
            num_intervals += num_loop
            least_counts = [count for count in least_counts if count > 0]

            if least_counts:
                num_empty = max(0, loop_size - num_loop)
                num_intervals += num_empty
            least_counts.sort()

        return num_intervals
