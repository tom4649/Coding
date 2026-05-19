class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_changes = [float("inf")] * (amount + 1)
        num_changes[0] = 0
        for target_amount in range(1, amount + 1):
            for coin in coins:
                if target_amount - coin >= 0:
                    num_changes[target_amount] = min(
                        num_changes[target_amount],
                        num_changes[target_amount - coin] + 1,
                    )

        return -1 if num_changes[amount] == float("inf") else num_changes[amount]
