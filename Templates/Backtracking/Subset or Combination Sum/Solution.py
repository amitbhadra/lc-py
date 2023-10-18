# https://leetcode.com/problems/combination-sum/description/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #candidates.sort()
        ret = []

        nums = []
        def helper(i, sum):
            if sum > target or i >= len(candidates):
                return
            if sum == target:
                ret.append(nums.copy())
                return
            nums.append(candidates[i])
            # include i and stay on i
            helper(i, sum+candidates[i])
            # # include i and move to next i
            # helper(i+1, sum+candidates[i])
            # don't include i and move to next i
            nums.pop()
            helper(i+1, sum)

        helper(0, 0)
        return ret
