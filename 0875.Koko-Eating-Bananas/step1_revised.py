import bisect


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if not piles:
            return 0

        def can_eat_all(k):
            return sum(((pile + k - 1) // k for pile in piles)) <= h

        max_candidate = max((max(piles) * 2 - 1) // (h // len(piles)), 1)
        min_candidate = max(min(piles) // h, 1)
        candidate = range(min_candidate, max_candidate + 1)
        index = bisect.bisect_left(
            range(len(candidate)), True, key=lambda index: can_eat_all(candidate[index])
        )
        return candidate[index]
