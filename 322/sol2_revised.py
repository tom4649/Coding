import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_changes = [float("inf")] * (
            amount + 1
        )  # the minimum number of coins required to make up amount i
        num_changes[0] = 0
        for target_amount in range(1, amount + 1):
            for coin in coins:
                if target_amount - coin >= 0:
                    num_changes[target_amount] = min(
                        num_changes[target_amount],
                        num_changes[target_amount - coin] + 1,
                    )

        return -1 if math.inf(num_changes[amount]) else num_changes[amount]
