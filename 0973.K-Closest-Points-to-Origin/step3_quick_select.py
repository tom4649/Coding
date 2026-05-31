import random


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def square_distance(point):
            return point[0] * point[0] + point[1] * point[1]

        def get_pivot_index(start, last):
            return start + random.randint(0, last - start)

        def partition(start, last, pivot_index):
            pivot_value = square_distance(points[pivot_index])
            points[pivot_index], points[last] = points[last], points[pivot_index]

            len_fixed = 0
            for i in range(start, last):
                if square_distance(points[i]) < pivot_value:
                    points[i], points[start + len_fixed] = (
                        points[start + len_fixed],
                        points[i],
                    )
                    len_fixed += 1

            points[last], points[start + len_fixed] = (
                points[start + len_fixed],
                points[last],
            )
            return start + len_fixed

        def k_closest_helper(start, last):
            if start >= last:
                return

            pivot_index_before = get_pivot_index(start, last)
            pivot_index_after = partition(start, last, pivot_index_before)

            if pivot_index_after == k:
                return
            elif pivot_index_after < k:
                return k_closest_helper(pivot_index_after + 1, last)
            else:
                return k_closest_helper(start, pivot_index_after - 1)

        k_closest_helper(0, len(points) - 1)
        return points[:k]
