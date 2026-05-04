import bisect


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

        minimum_value = max(weights)
        maximum_value = sum(weights)

        return (
            bisect.bisect_left(range(minimum_value, maximum_value), True, key=can_ship)
            + minimum_value
        )
