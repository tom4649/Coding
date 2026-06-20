class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if not piles:
            return 0

        def can_eat_all(k):
            hours = 0
            for i, pile in enumerate(piles):
                hours += (pile + k - 1) // k
                if hours + (len(piles) - i - 1) > h:
                    return False
            return True

        left = max(min(piles) // h, 1)
        right = max((max(piles) * 2 - 1) // (h // len(piles)), 1) + 1
        while left < right:
            mid = left + (right - left) // 2
            if not can_eat_all(mid):
                left = mid + 1
            else:
                right = mid

        return left
