# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description/

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minPos = maxPos = 0
        minVal = maxVal = nums[0]

        for i, num in enumerate(nums):
            if num < minVal:
                minVal = num
                minPos = i
            elif num >= maxVal:
                maxVal = num
                maxPos = i

        if maxPos < minPos:
            return minPos + (len(nums) - 1 - maxPos) - 1
        else:
            return minPos + (len(nums) - 1 - maxPos)
