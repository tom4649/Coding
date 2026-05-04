from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins_sorted = sorted(coins)
        visited = [False] * (amount + 1)
        visited[0] = True

        frontier = deque([0])
        steps = 0

        while frontier:
            steps += 1
            len_current_frontier = len(frontier)
            for _ in range(len_current_frontier):
                current_sum = frontier.popleft()
                for coin in coins_sorted:
                    next_sum = current_sum + coin
                    if next_sum > amount:
                        break
                    if visited[next_sum]:
                        continue
                    if next_sum == amount:
                        return steps
                    visited[next_sum] = True
                    frontier.append(next_sum)

        return -1
