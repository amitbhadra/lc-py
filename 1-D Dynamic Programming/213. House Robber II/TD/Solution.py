class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        #dp = [-1 for _ in range(len(nums))]

        def helper(dp, n, searchLast=True):
            if searchLast and n < 0: return 0
            elif not searchLast and n < 1: return 0

            if dp[n] != -1: return dp[n]

            dp[n] = max(nums[n] + helper(dp, n-2, searchLast), helper(dp, n-1, searchLast))
            return dp[n]

        return max(helper([-1 for _ in range(len(nums))], len(nums)-1, False), helper([-1 for _ in range(len(nums))], len(nums)-2))
