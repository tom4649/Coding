import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = collections.Counter(tasks)
        counts = list(counter.values())

        max_count = max(counts)
        max_count_kinds = counts.count(max_count)

        empty_slots_per_part = n + 1 - max_count_kinds
        total_empty_slots = empty_slots_per_part * (max_count - 1)
        available_tasks = len(tasks) - (max_count_kinds * max_count)

        idles = max(0, total_empty_slots - available_tasks)

        return len(tasks) + idles
