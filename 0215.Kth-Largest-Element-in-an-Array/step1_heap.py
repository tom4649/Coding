import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, n)
            else:
                heapq.heappush(heap, n)

        return heapq.heappop(heap)
