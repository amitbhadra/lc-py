# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0
        for num in nums:
            sum += num
            maxSum = max(sum, maxSum)
            sum = max(sum, 0)
        return maxSum
