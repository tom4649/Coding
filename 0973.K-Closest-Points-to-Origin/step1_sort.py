class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def square_distance_to_origin(point):
            return point[0] ** 2 + point[1] ** 2

        ordered_points = sorted(points, key=square_distance_to_origin)
        return ordered_points[:k]
