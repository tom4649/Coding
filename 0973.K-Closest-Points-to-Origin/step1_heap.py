import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def square_distance_to_origin(point):
            return point[0] ** 2 + point[1] ** 2

        heap = [(square_distance_to_origin(point), i) for i, point in enumerate(points)]
        heapq.heapify(heap)

        k_closest = []
        while k > 0:
            _, i = heapq.heappop(heap)
            k_closest.append(points[i])
            k -= 1

        return k_closest
