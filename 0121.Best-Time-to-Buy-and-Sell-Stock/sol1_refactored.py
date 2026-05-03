class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = -float("inf")
        max_profit = 0
        for price in prices[::-1]:
            max_price = max(max_price, price)
            max_profit = max(max_profit, max_price - price)

        return max_profit
