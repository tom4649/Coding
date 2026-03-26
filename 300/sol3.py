from bisect import bisect_left


class SegTree:
    def __init__(self, size):
        n = 1
        while n < size:
            n *= 2
        self.offset = n
        self.data = [0] * 2 * n

    def _to_leaf_index(self, index):
        return index + self.offset - 1

    def update(self, rank, value):
        k = self._to_leaf_index(rank)
        self.data[k] = max(self.data[k], value)
        k //= 2
        while k >= 1:
            self.data[k] = max(self.data[2 * k], self.data[2 * k + 1])
            k //= 2

    def query(self, first_rank, last_rank):
        if first_rank > last_rank:
            return 0
        l, r = self._to_leaf_index(first_rank), self._to_leaf_index(last_rank)
        result = 0
        while l <= r:
            if l % 2 == 1:
                result = max(result, self.data[l])
                l += 1
            if r % 2 == 0:
                result = max(result, self.data[r])
                r -= 1
            l //= 2
            r //= 2
        return result


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_sorted = sorted(set(nums))

        def num_to_rank(n):
            return bisect_left(nums_sorted, n) + 1

        seg_tree = SegTree(len(nums))

        max_len = 0
        for n in nums:
            rank = num_to_rank(n)
            max_len_with_smaller = seg_tree.query(1, rank - 1)
            seg_tree.update(rank, max_len_with_smaller + 1)
            max_len = max(max_len, max_len_with_smaller + 1)

        return max_len
