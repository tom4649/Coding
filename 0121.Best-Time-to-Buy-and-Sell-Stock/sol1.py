class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price_in_current_or_future = -float("inf")
        max_profits = []
        for price in prices[::-1]:
            max_price_in_current_or_future = max(max_price_in_current_or_future, price)
            max_profits.append(max_price_in_current_or_future - price)

        return max(max_profits)
