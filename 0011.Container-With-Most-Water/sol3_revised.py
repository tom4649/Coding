import heapq


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 負値にすることでmin-heapの順序を高さの降順（max-heap）として扱う
        neg_height_index_pairs = [(-h, i) for i, h in enumerate(height)]
        heapq.heapify(neg_height_index_pairs)

        max_amount = 0
        min_pos = float("inf")
        max_pos = float("-inf")

        while neg_height_index_pairs:
            neg_h, i = heapq.heappop(neg_height_index_pairs)
            h = -neg_h

            min_pos = min(min_pos, i)
            max_pos = max(max_pos, i)

            max_amount = max(max_amount, h * (max_pos - min_pos))

        return max_amount
