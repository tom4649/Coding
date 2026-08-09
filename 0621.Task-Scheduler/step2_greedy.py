import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = collections.Counter(tasks)
        counts = sorted(counter.values(), reverse=True)

        max_freq = counts[0]
        chunk_count = max_freq - 1

        total_idle = chunk_count * n

        for freq in counts[1:]:
            total_idle -= min(chunk_count, freq)

        return len(tasks) + max(0, total_idle)
