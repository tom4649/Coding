import heapq


class MedianFinder:
    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if len(self.low) > len(self.high):
            if num >= self.low[0]:
                heapq.heappush(self.high, num)
            else:
                max_low = heapq.heappop_max(self.low)
                heapq.heappush(self.high, max_low)
                heapq.heappush_max(self.low, num)
        else:
            if not self.high or num <= self.high[0]:
                heapq.heappush_max(self.low, num)
            else:
                min_high = heapq.heappop(self.high)
                heapq.heappush_max(self.low, min_high)
                heapq.heappush(self.high, num)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return self.low[0]
        return (self.low[0] + self.high[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
