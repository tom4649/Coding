import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def transform(n):
            return (n <= nums[-1], n >= target)
