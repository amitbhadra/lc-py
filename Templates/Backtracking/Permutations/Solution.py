# https://leetcode.com/problems/permutations/description/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        if len(nums) == 1:  return [nums[:]] # time optimization over nums.copy()

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            ret.extend(perms)
            nums.append(n)
        
        return ret
