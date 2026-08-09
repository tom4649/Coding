import heapq


class Solution:
    def maxArea(self, height: list[int]) -> int:
        negative_height_index_pairs = [(-h, i) for i, h in enumerate(height)]
        heapq.heapify(negative_height_index_pairs)

        min_index = len(height)
        max_index = -1
        max_area = 0

        while negative_height_index_pairs:
            negative_h, index = heapq.heappop(negative_height_index_pairs)
            min_index = min(min_index, index)
            max_index = max(max_index, index)
            max_area = max(max_area, -negative_h * (max_index - min_index))

        return max_area
