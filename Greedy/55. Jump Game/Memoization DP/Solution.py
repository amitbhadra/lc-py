# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/description/
# Gets TLE for recursive + memo but accepted for Bottom Up iterative

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1] * len(nums)
        N = len(nums) - 1
        def helper(idx):
            if idx >= N:    return True
            elif dp[idx] != -1: return dp[idx]
            elif nums[idx] == 0:    return False
            val = False
            dp[idx] = any(helper(idx + num) for num in range(1, nums[idx] + 1))
            return dp[idx]

        return helper(0)
