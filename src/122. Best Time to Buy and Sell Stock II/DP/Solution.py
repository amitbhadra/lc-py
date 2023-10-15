class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def maxProfitFromDay(day, haveStock):
            if day == len(prices):
                return 0

            if (day, haveStock) in memo:
                return memo[(day, haveStock)]
            if haveStock:
                memo[(day, haveStock)] = max(
                    maxProfitFromDay(day + 1, False) + prices[day],  # sell
                    maxProfitFromDay(day + 1, True)  # rest
                )
            else:
                memo[(day, haveStock)] = max(
                    maxProfitFromDay(day + 1, True) - prices[day],  # buy
                    maxProfitFromDay(day + 1, False)  # rest
                )
            return memo[(day, haveStock)]

        # Initial call: day 0, no stocks
        return maxProfitFromDay(0, False)
