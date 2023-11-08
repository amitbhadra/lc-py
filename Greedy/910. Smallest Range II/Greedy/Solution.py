# https://leetcode.com/problems/smallest-range-ii/description/

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]

        for idx in range(len(nums) - 1):
            # assuming that nums[idx] is the max val
            min_val = min(nums[0] + k, nums[idx + 1] - k) # idx + 1 because we need to consider last idx
            max_val = max(nums[idx] + k, nums[-1] - k)
            res = min(res, max_val - min_val)

        return res
