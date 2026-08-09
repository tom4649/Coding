import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = collections.Counter(tasks)
        counts = list(counter.values())

        max_count = max(counts)
        num_max_kinds = counts.count(max_count)

        num_others = len(tasks) - (num_max_kinds * max_count)
        total_empty = max(0, (n + 1 - num_max_kinds) * (max_count - 1) - num_others)

        return len(tasks) + total_empty
