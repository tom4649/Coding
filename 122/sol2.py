class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            raise ValueError("The input list is empty")

        profit_holding_stock = -prices[0]
        profit_not_holding_stock = 0
        for price in prices[1:]:
            next_profit_holding_stock = max(
                profit_holding_stock, profit_not_holding_stock - price
            )
            next_profit_not_holding_stock = max(
                profit_not_holding_stock, profit_holding_stock + price
            )
            profit_holding_stock, profit_not_holding_stock = (
                next_profit_holding_stock,
                next_profit_not_holding_stock,
            )

        return profit_not_holding_stock
