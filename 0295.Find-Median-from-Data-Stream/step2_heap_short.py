import heapq


class MedianFinder:
    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.high, num)
        min_high = heapq.heappop(self.high)
        heapq.heappush_max(self.low, min_high)
        if len(self.low) > len(self.high) + 1:
            max_low = heapq.heappop_max(self.low)
            heapq.heappush(self.high, max_low)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return self.low[0]
        return (self.low[0] + self.high[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
