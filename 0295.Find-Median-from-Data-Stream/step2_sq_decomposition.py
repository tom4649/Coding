import math


class MedianFinder:
    def __init__(self):
        # 値の範囲は -100,000 ～ 100,000
        # 負の数を扱うため、+100000 のオフセットを適用
        self.offset = 100000
        self.MAX_VAL = 200005

        # ブロックサイズ（√200005 ≒ 447 なので、余裕を持って 450 とする）
        self.block_size = int(math.sqrt(self.MAX_VAL)) + 1

        # 各数字の出現回数を記録する配列 (1次元目)
        self.counts = [0] * (self.MAX_VAL + 1)

        # 各ブロック内の数字の総数を記録する配列 (2次元目)
        self.blocks = [0] * (self.MAX_VAL // self.block_size + 1)

        self.total_count = 0

    def addNum(self, num: int) -> None:
        idx = num + self.offset

        # 該当する数字のカウントと、その数字が属するブロックのカウントを増やす
        self.counts[idx] += 1
        self.blocks[idx // self.block_size] += 1
        self.total_count += 1

    def _find_kth(self, k: int) -> int:
        """通算で k 番目の要素（インデックス）を平方分割のバケットを使って探す"""
        block_idx = 0

        # 1. まずは「ブロック単位」で大雑把にスキップする
        # k番目の要素が、どのブロックに含まれているかを特定する
        while block_idx < len(self.blocks) and k > self.blocks[block_idx]:
            k -= self.blocks[block_idx]
            block_idx += 1

        # 2. ターゲットのブロックが見つかったら、その中を「1マスずつ」泥臭く探す
        start_idx = block_idx * self.block_size
        for idx in range(start_idx, start_idx + self.block_size):
            k -= self.counts[idx]
            if k <= 0:
                return idx

        return 0

    def findMedian(self) -> float:
        if self.total_count % 2 == 1:
            # 奇数個の場合
            kth_idx = self._find_kth((self.total_count // 2) + 1)
            return float(kth_idx - self.offset)
        else:
            # 偶数個の場合
            left_idx = self._find_kth(self.total_count // 2)
            right_idx = self._find_kth((self.total_count // 2) + 1)
            return (left_idx + right_idx - 2 * self.offset) / 2.0
