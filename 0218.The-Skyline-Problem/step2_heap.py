import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        if not buildings:
            return []

        heap = [(0, float("inf"))]
        key_points = []
        i = 0

        while i < len(buildings) or len(heap) > 1:
            next_start = buildings[i][0] if i < len(buildings) else float("inf")
            next_end = heap[0][1]
            x = min(next_start, next_end)

            while i < len(buildings) and buildings[i][0] == x:
                _, right, height = buildings[i]
                heapq.heappush(heap, (-height, right))
                i += 1

            while heap[0][1] <= x:
                heapq.heappop(heap)

            height = -heap[0][0]
            if not key_points or key_points[-1][1] != height:
                key_points.append([x, height])

        return key_points
