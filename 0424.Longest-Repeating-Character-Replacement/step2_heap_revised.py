import collections
import heapq


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        left = 0
        length_of_longest = 0
        heap = []  # contains (count, alphabet) in max heap

        def get_max_count():
            while heap[0][0] != count[heap[0][1]]:
                heapq.heappop_max(heap)
            return heap[0][0]

        for right in range(len(s)):
            count[s[right]] += 1
            heapq.heappush_max(heap, (count[s[right]], s[right]))

            while (right - left + 1) - get_max_count() > k:
                count[s[left]] -= 1
                heapq.heappush_max(heap, (count[s[left]], s[left]))
                left += 1

            length_of_longest = max(length_of_longest, right - left + 1)

        return length_of_longest
