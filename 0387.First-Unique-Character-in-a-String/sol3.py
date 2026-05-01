import queue


class Solution:
    def firstUniqChar(self, s: str) -> int:
        import queue
        from collections import defaultdict

        counts = defaultdict(int)
        count_and_idxs = queue.Queue()

        for i, c in enumerate(s):
            counts[c] += 1
            count_and_idxs.put((c, i))

            while not count_and_idxs.empty():
                front_c, _front_i = count_and_idxs.queue[0]
                if counts[front_c] == 1:
                    break
                count_and_idxs.get()

        return count_and_idxs.queue[0][1] if not count_and_idxs.empty() else -1
