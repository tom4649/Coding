import bisect


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k):
            return sum(((pile + k - 1) // k for pile in piles)) <= h

        candidate = range(
            max(min(piles) // h, 1),
            max((max(piles) * 2 - 1) // (h // len(piles)), 1) + 1,
        )
        index = bisect.bisect_left(
            range(len(candidate)), True, key=lambda index: can_eat_all(candidate[index])
        )
        return candidate[index]
