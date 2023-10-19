class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = set()

        def helper(i):
            if i == len(nums):
                return
            subset.append(nums[i])
            helper(i+1)
            ret.add(tuple(sorted(subset[:])))
            subset.pop()
            helper(i+1)
            ret.add(tuple(sorted(subset[:])))

        subset = []
        helper(0)

        return ret
