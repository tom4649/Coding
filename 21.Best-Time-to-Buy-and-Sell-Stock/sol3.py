import itertools


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            raise ValueError("The input list is empty")

        min_prices = itertools.accumulate(prices, min)
        max_profit = [
            price - min_price for (price, min_price) in zip(prices, min_prices)
        ]
        return max(max_profit)
