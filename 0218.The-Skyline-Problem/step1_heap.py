import collections
import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        xs = set()
        starts = collections.defaultdict(list)
        for l, r, h in buildings:
            xs.add(l)
            xs.add(r)
            starts[l].append((h, r))

        key_points = []
        heap = [(0, float("inf"))]
        sorted_xs = sorted(xs)
        for x in sorted_xs:
            for h, r in starts[x]:
                heapq.heappush(heap, (-h, r))

            while heap[0][1] <= x:
                heapq.heappop(heap)

            height = - heap[0][0]
            if not key_points or key_points[-1][1] != height:
                key_points.append((x, height))

        return key_points



