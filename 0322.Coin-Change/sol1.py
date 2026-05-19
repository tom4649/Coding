import functools


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.cache
        def minimum_coins(target_amount):
            if target_amount == 0:
                return 0
            if target_amount < 0:
                return float("inf")
            return min([minimum_coins(target_amount - coin) + 1 for coin in coins])

        num_changes = minimum_coins(amount)
        return -1 if num_changes == float("inf") else num_changes
