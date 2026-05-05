from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minimum_coins = [float("inf")] * (amount + 1)
        minimum_coins[0] = 0
        coins_sorted = sorted(coins)

        frontier = deque([0])
        visited = {0}

        while frontier:
            current_sum = frontier.popleft()
            for coin in coins_sorted:
                next_sum = current_sum + coin
                if next_sum in visited or next_sum > amount:
                    continue
                minimum_coins[next_sum] = min(
                    minimum_coins[next_sum], minimum_coins[current_sum] + 1
                )
                frontier.append(next_sum)
                visited.add(current_sum)

        return -1 if minimum_coins[amount] == float("inf") else minimum_coins[amount]
