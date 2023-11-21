# https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i, num in enumerate(nums):
            for k, val in enumerate(nums[:i]):
                if val<num and dp[i]<=dp[k]:
                    dp[i] = dp[k]+1
        return max(dp)
