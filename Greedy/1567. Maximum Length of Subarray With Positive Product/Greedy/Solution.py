# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/description/

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for num in nums:
            # if num is positive, we increment pos and neg only of neg exists
            if num > 0:
                pos = 1 + pos
                neg = 1 + neg if neg else 0
            # if num is negative, we replace pos with neg + 1 as negative will turn to positive
            # and we replace neg with pos + 1 for the same reason
            # This needs to be in 1 line otherwise temp var needs to be used 
            elif num < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            # 0 acts as separator
            else:
                pos = neg = 0
            ans = max(ans, pos)
        return ans
