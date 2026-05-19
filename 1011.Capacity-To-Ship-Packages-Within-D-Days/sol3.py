from unicodedata import mirrored


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity):
            used_days = 1
            total_weight = 0
            for weight in weights:
                if total_weight + weight <= capacity:
                    total_weight += weight
                    continue
                used_days += 1
                if used_days > days or weight > capacity:
                    return False
                total_weight = weight
            return True

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if not can_ship(mid):
                left = mid + 1
            else:
                right = mid
        return left
