import heapq
import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s

        counter = collections.Counter(s)
        most_common = counter.most_common()

        if most_common[0][1] > (len(s) - 1) // 2 + 1:
            return ""

        count_and_letter = [(count, c) for (c, count) in most_common]
        heapq.heapify_max(count_and_letter)
        result = []

        while len(result) < len(s):
            count, c = heapq.heappop_max(count_and_letter)
            result.append(c)
            count_next = 0
            if len(count_and_letter) > 0:
                count_next, c_next = heapq.heappop_max(count_and_letter)
                result.append(c_next)
            if count > 1:
                heapq.heappush_max(count_and_letter, (count - 1, c))
            if count_next > 1:
                heapq.heappush_max(count_and_letter, (count_next - 1, c_next))

        return "".join(result)
