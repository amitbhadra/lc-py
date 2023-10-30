class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numsSet = set(nums)
        if 0 in numsSet:    return len(numsSet) - 1
        else:   return len(numsSet)
