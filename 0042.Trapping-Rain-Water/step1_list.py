import itertools


class Solution:
    def trap(self, height: list[int]) -> int:
        max_from_left = itertools.accumulate(height, max)
        max_from_right = reversed(list(itertools.accumulate(reversed(height), max)))

        difference_max_left = [m - h for m, h in zip(max_from_left, height)]
        difference_max_right = [m - h for m, h in zip(max_from_right, height)]

        water_trapped = 0
        for left, right in zip(difference_max_left, difference_max_right):
            water_trapped += min(left, right)

        return water_trapped
