class MedianFinder:
    def __init__(self):
        # 値の範囲は -100,000 ～ 100,000
        # 1ベースのインデックスにするため、+100001 のオフセットを適用
        self.offset = 100001
        self.MAX_VAL = 200005  # 十分なBITのサイズ

        self.bit = [0] * (self.MAX_VAL + 1)
        self.total_count = 0

    def _add(self, idx: int, val: int) -> None:
        """BITに値を加算する"""
        while idx <= self.MAX_VAL:
            self.bit[idx] += val
            idx += idx & -idx

    def _find_kth(self, k: int) -> int:
        """累積和が k 以上になる最小のインデックス（値）を二分探索（倍増法）で探す"""
        idx = 0
        # MAX_VALを超えない最大の2のべき乗からスタート (2^17 = 131072, 2^18 = 262144)
        shift = 1 << 17

        while shift > 0:
            if idx + shift <= self.MAX_VAL and self.bit[idx + shift] < k:
                idx += shift
                k -= self.bit[idx]  # 既に超えた分のカウントを引く
            shift >>= 1

        # idx + 1 が、累積和が初めて k 以上になる位置
        return idx + 1

    def addNum(self, num: int) -> None:
        # 負の数を考慮してインデックスをシフト
        bit_idx = num + self.offset
        self._add(bit_idx, 1)
        self.total_count += 1

    def findMedian(self) -> float:
        if self.total_count % 2 == 1:
            # 奇数個の場合：真ん中（(n // 2) + 1 番目）の要素を返す
            kth_idx = self._find_kth((self.total_count // 2) + 1)
            return float(kth_idx - self.offset)
        else:
            # 偶数個の場合：(n // 2) 番目と (n // 2 + 1) 番目の要素の平均を返す
            left_idx = self._find_kth(self.total_count // 2)
            right_idx = self._find_kth((self.total_count // 2) + 1)
            return (left_idx + right_idx - 2 * self.offset) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
