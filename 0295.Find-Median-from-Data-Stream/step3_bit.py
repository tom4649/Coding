class MedianFinder:
    def __init__(self):
        self.offset = 100001
        self.MAX_VAL = 200005
        self.bit = [0] * (self.MAX_VAL + 1)
        self.total_count = 0

    def _add(self, idx: int, val: int) -> None:
        while idx <= self.MAX_VAL:
            self.bit[idx] += val
            idx += idx & -idx

    def _find_kth(self, k: int) -> int:
        idx = 0
        shift = 1 << 17

        while shift > 0:
            if idx + shift <= self.MAX_VAL and self.bit[idx + shift] < k:
                idx += shift
                k -= self.bit[idx]
            shift >>= 1
        return idx + 1

    def addNum(self, num: int) -> None:
        bit_idx = num + self.offset
        self._add(bit_idx, 1)
        self.total_count += 1

    def findMedian(self) -> float:
        if self.total_count % 2 == 1:
            kth_idx = self._find_kth((self.total_count // 2) + 1)
            return float(kth_idx - self.offset)
        else:
            left_idx = self._find_kth(self.total_count // 2)
            right_idx = self._find_kth((self.total_count // 2) + 1)
            return (left_idx + right_idx - 2 * self.offset) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
