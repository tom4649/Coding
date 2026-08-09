import bisect


class MedianFinder:
    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.data, num)

    def findMedian(self) -> float:
        middle_index = len(self.data) // 2
        if len(self.data) % 2 == 0:
            return (self.data[middle_index - 1] + self.data[middle_index]) / 2
        return self.data[middle_index]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
