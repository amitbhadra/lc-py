class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(n, dp):
            if n <= 1: 
                dp[n] = cost[n]
                return dp[n]
            if dp[n] != -1: return dp[n]
            dp[n] = min(helper(n-1, dp), helper(n-2, dp)) + cost[n]
            return dp[n]

        dp = [-1] * len(cost)
        return min(helper(len(cost)-1, dp), helper(len(cost)-2, dp))
