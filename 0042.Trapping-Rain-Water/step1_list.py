import itertools


class Solution:
    def trap(self, height: list[int]) -> int:
        max_from_left = itertools.accumulate(height, max)
        max_from_right = reversed(list(itertools.accumulate(reversed(height), max)))

        difference_max_left = [m - h for m, h in zip(max_from_left, height)]
        difference_max_right = [m - h for m, h in zip(max_from_right, height)]

        trapped_water = 0
        for left, right in zip(difference_max_left, difference_max_right):
            trapped_water += min(left, right)

        return trapped_water
