# rootのindexは1
# 親ノード: i // 2
# 子ノード: (i * 2), (i * 2 + 1)
class SegmentTree:
    def __init__(self, nums):
        self.size = 1
        while self.size < len(nums):
            self.size *= 2
        self.tree = [(float("inf"), 0)] * (self.size * 2)
        # 葉に値をセット
        for i, num in enumerate(nums):
            self.tree[self.size + i] = (num, i)
        # ノードを更新
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    # トップダウン
    def query_recursive(self, begin, end, node=1, node_begin=0, node_end=-1):
        if node_end == -1:
            node_end = self.size
        if node_end <= begin or end <= node_begin:
            return (float("inf"), 0)
        if begin <= node_begin and node_end <= end:
            return self.tree[node]

        node_middle = (node_begin + node_end) // 2
        left_min = self.query_recursive(begin, end, node * 2, node_begin, node_middle)
        right_min = self.query_recursive(
            begin, end, node * 2 + 1, node_middle, node_end
        )
        return min(left_min, right_min)

    # ボトムアップ
    def query(self, left, right):
        left += self.size
        right += self.size
        min_node = (float("inf"), 0)
        while left < right:
            if left % 2 == 1:
                # 親ノードは範囲外なので右に移動
                min_node = min(min_node, self.tree[left])
                left += 1
            if right % 2 == 1:
                # 親ノードは範囲外なので左に移動
                right -= 1
                min_node = min(min_node, self.tree[right])
            left //= 2
            right //= 2
        return min_node


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        segment_tree = SegmentTree(heights)

        def calculate_area_with_minimum_height_between(begin, end):
            if begin >= end:
                return 0
            # min_height, min_index = segment_tree.query(begin, end)
            min_height, min_index = segment_tree.query_recursive(begin, end)
            area = min_height * (end - begin)
            max_area = max(
                area,
                calculate_area_with_minimum_height_between(begin, min_index),
                calculate_area_with_minimum_height_between(min_index + 1, end),
            )
            return max_area

        return calculate_area_with_minimum_height_between(0, len(heights))
