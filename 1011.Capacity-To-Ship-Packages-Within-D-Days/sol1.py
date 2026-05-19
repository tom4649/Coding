import bisect

MAXIMUM_WEIGHT = 500


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity):
            used_days = 1
            shipped_weight_on_current_day = 0
            for weight in weights:
                if shipped_weight_on_current_day + weight <= capacity:
                    shipped_weight_on_current_day += weight
                    continue
                used_days += 1
                if used_days > days or weight > capacity:
                    return False
                shipped_weight_on_current_day = weight
            return True

        maximum_value = min(sum(weights), MAXIMUM_WEIGHT * (len(weights) // days + 1))

        return bisect.bisect_left(range(1, maximum_value), True, key=can_ship) + 1
