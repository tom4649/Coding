import itertools


class Solution:
    def trap(self, height: list[int]) -> int:
        max_heights_from_left = itertools.accumulate(height, max)
        max_heights_from_right = reversed(
            list(itertools.accumulate(reversed(height), max))
        )

        return sum(
            min(m_left, m_right) - h
            for m_left, m_right, h in zip(
                max_heights_from_left, max_heights_from_right, height
            )
        )
