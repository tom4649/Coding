import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def square_distance_to_origin(point):
            return point[0] ** 2 + point[1] ** 2

        max_heap = []
        for point in points:
            if len(max_heap) < k:
                heapq.heappush_max(
                    max_heap,
                    (square_distance_to_origin(point), point),
                )
            else:
                heapq.heappushpop_max(
                    max_heap, (square_distance_to_origin(point), point)
                )

        return [point for _, point in max_heap]
