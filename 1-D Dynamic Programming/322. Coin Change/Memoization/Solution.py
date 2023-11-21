# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        for i in coins:
            dp[i] = 1
        
        def getResult(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            
            k = float("inf")
            for i in coins:
                if i<=amount:
                    k = min(k,1 + getResult(amount-i))
            
            dp[amount] = k
            return dp[amount]
        
        k = getResult(amount)
        return k if k!=float("inf") else -1
