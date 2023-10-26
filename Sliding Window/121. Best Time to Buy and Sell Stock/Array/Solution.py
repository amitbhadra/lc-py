class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought, sold = prices[0], prices[0] - 1
        profit = 0
        for price in prices[1:]:
            if price < bought:
                profit = max((sold-bought), profit)
                bought = price
                sold = price - 1
            elif price > sold:
                sold = price
                
        profit = max((sold-bought), profit)
        return profit
