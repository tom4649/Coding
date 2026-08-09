import math


class MedianFinder:
    def __init__(self):
        self.offset = 100000
        self.MAX_VAL = 200005
        self.block_size = int(math.sqrt(self.MAX_VAL)) + 1
        self.counts = [0] * (self.MAX_VAL + 1)
        self.blocks = [0] * (self.MAX_VAL // self.block_size + 1)
        self.total_count = 0

    def addNum(self, num: int) -> None:
        idx = num + self.offset
        self.counts[idx] += 1
        self.blocks[idx // self.block_size] += 1
        self.total_count += 1

    def _find_kth(self, k: int) -> int:
        block_idx = 0
        while block_idx < len(self.blocks) and k > self.blocks[block_idx]:
            k -= self.blocks[block_idx]
            block_idx += 1
        start_idx = block_idx * self.block_size
        for idx in range(start_idx, start_idx + self.block_size):
            k -= self.counts[idx]
            if k <= 0:
                return idx
        return 0

    def findMedian(self) -> float:
        if self.total_count % 2 == 1:
            kth_idx = self._find_kth((self.total_count // 2) + 1)
            return float(kth_idx - self.offset)
        else:
            left_idx = self._find_kth(self.total_count // 2)
            right_idx = self._find_kth((self.total_count // 2) + 1)
            return (left_idx + right_idx - 2 * self.offset) / 2.0
