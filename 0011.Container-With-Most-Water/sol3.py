import heapq


class Solution:
    def maxArea(self, height: List[int]) -> int:
        heap = [(-h, i) for i, h in enumerate(height)]
        heapq.heapify(heap)

        max_amount = 0
        min_pos = float("inf")
        max_pos = float("-inf")

        while heap:
            neg_h, i = heapq.heappop(heap)
            h = -neg_h

            min_pos = min(min_pos, i)
            max_pos = max(max_pos, i)

            max_amount = max(max_amount, h * (max_pos - min_pos))

        return max_amount
