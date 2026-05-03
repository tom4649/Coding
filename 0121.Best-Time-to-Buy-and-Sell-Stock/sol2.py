class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_in_current_or_past = float("inf")
        max_profits = []
        for price in prices:
            min_price_in_current_or_past = min(min_price_in_current_or_past, price)
            max_profits.append(price - min_price_in_current_or_past)

        return max(max_profits)
