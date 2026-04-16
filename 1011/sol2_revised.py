import bisect


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

        minimum_value = max(weights)
        maximum_value = sum(weights)

        return (
            bisect.bisect_left(range(minimum_value, maximum_value), True, key=can_ship)
            + minimum_value
        )
