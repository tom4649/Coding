# 11. Container With Most Water

総当たりの解が思いつくがおおよそ O(n^2), 10^3 の実行時間の見積もり
書いてみたがTLE: sol1.py

LeetCodeのヒント2を見る

> Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.

なるほど、これを見てやっとわかった: sol2.py

つまり、
ポインタ start, lastがあり、max_areaがstartとそれよりも左側、lastとそれよりも右側を端に持つ場合を含めた最大値を持つとする
このとき、max_areaが更新されうるのは、min(height[start], height[last])が増加したときのみ

時間計算量 O(n)

### 他の人のコード

https://github.com/thonda28/leetcode/pull/16#discussion_r1694270587

segment木を用いた実装とbisectを用いた実装

segment木を使う方針は持てるようになりたい


セグメント木を用いた実装: O((n+h)logh) (h = max(height))

```python
import math
from typing import Callable, Iterable, List


class SegmentTree:
    def __init__(self, nums: List[int], func: Callable[[Iterable[int]], int], default_value: int):
        self.func = func
        self.default_value = default_value
        x = 1
        while x < len(nums):
            x *= 2
        self.n = x
        self.tree = [self.default_value] * (2 * self.n - 1)

        for index in range(len(nums)):
            self.update(index, nums[index])

    def update(self, index: int, value: int):
        index += self.n - 1
        self.tree[index] = value
        while index > 0:
            index = (index - 1) // 2
            self.tree[index] = self.func([self.tree[2 * index + 1], self.tree[2 * index + 2]])

    def range_query(self, begin: int, end: int) -> int:
        return self.__sub_query(begin, end, 0, 0, self.n)

    def __sub_query(self, begin: int, end: int, index: int, left: int, right: int) -> int:
        if end <= left or right <= begin:
            return self.default_value
        if begin <= left and right <= end:
            return self.tree[index]
        mid = (left + right) // 2
        val1 = self.__sub_query(begin, end, index * 2 + 1, left, mid)
        val2 = self.__sub_query(begin, end, index * 2 + 2, mid, right)
        return self.func([val1, val2])


class Solution:
    def swap_index_value(self, nums: List[int], use_last_seen: bool, default_value: int) -> List[int]:
        n = len(nums)
        swapped_list = [default_value] * (max(nums) + 1)
        start, stop, step = (0, n, 1) if use_last_seen else (n - 1, -1, -1)

        for index in range(start, stop, step):
            swapped_list[nums[index]] = index

        return swapped_list

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_height = max(height)
        max_amount = 0

        last_seen_map = self.swap_index_value(height, use_last_seen=True, default_value=-math.inf)
        max_seg_tree = SegmentTree(last_seen_map, func=max, default_value=-math.inf)
        for left in range(n):
            left_height = height[left]
            right = max_seg_tree.range_query(left_height, max_height + 1)
            max_amount = max(max_amount, left_height * (right - left))

        first_seen_map = self.swap_index_value(height, use_last_seen=False, default_value=math.inf)
        min_seg_tree = SegmentTree(first_seen_map, func=min, default_value=math.inf)
        for right in range(n - 1, -1, -1):
            right_height = height[right]
            left = min_seg_tree.range_query(right_height, max_height + 1)
            max_amount = max(max_amount, right_height * (right - left))

        return max_amount
```

bisectを用いた実装

計算量O(n log n)

高さのボトルネックが左側、右側になる場合を分けて考える。
その逆側のindexは「自分より端に近い方に自分以上の高さがない」ものだけを考えればよい（`generate_necessary_height_with_indices`）

```python
import bisect
from typing import List, Tuple


class Solution:
    def maxArea(self, height: List[int]) -> int:

        def generate_necessary_height_with_indices(height: List[int], reverse: bool) -> List[Tuple[int, int]]:
            start, stop, step = (n - 1, -1, -1) if reverse else (0, n, 1)

            necessary_height_with_indices = [(-1, -1)]
            for i in range(start, stop, step):
                if necessary_height_with_indices[-1][0] < height[i]:
                    necessary_height_with_indices.append((height[i], i))
            return necessary_height_with_indices

        n = len(height)
        max_amount = 0

        necessary_right_height_with_indices = generate_necessary_height_with_indices(height, reverse=True)
        for left in range(n):
            i = bisect.bisect_left(
                necessary_right_height_with_indices,
                True,
                key=lambda x: x[0] >= height[left]
            )
            right = necessary_right_height_with_indices[i][1]
            max_amount = max(max_amount, (right - left) * height[left])

        necessary_left_height_with_indices = generate_necessary_height_with_indices(height, False)
        for right in range(n - 1, -1, -1):
            i = bisect.bisect_left(
                necessary_left_height_with_indices,
                True,
                key=lambda x: x[0] >= height[right]
            )
            left = necessary_left_height_with_indices[i][1]
            max_amount = max(max_amount, (right - left) * height[right])

        return max_amount
```

https://github.com/usatie/leetcode/commit/e5ab842a5819b4159feb7dff69f2d9d74504457d

> (高さ, 位置) で heap に突っ込んでおいて、取り出していくと、高さが H 以上の棒の位置の配置が出てくるので、その配置から高さ H での水の最大の入れ方が出てきます。

heapでも解けるのか。自分の選択肢がいかに狭いかよくわかる
これを書いてみる: sol3.py
高さの大きい順に取り出していけば高さはその取り出した長さで確定するため最左と最右のindexを用いることができる
時間計算量O(nlog n)
