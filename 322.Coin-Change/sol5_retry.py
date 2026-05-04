class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        if amount == 0:
            return 0

        frontier = [0]
        visited = {0}
        count_coin = 1

        while frontier:
            next_frontier = []
            for total in frontier:
                for coin in coins:
                    next_total = total + coin
                    if next_total == amount:
                        return count_coin
                    if next_total in visited or next_total > amount:
                        continue
                    next_frontier.append(next_total)
                    visited.add(next_total)
            frontier = next_frontier
            count_coin += 1
        return -1
