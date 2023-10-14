class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(n, dp):
            if n < 0: return 0
            if dp[n] != -1: return dp[n]
            dp[n] = max(helper(n-2, dp) + nums[n], helper(n-1, dp)) 
            return dp[n]

        if len(nums) <= 2: return max(nums)
        dp = [-1 for _ in range(len(nums))]
        return helper(len(nums)-1, dp)
