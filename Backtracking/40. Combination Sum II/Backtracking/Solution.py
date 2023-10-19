# Normal backtracking gives TLE so there's a dupe optimization
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = set()
        candidates.sort()
        subset = []
        def helper(i, sum):
            if sum == target:
                ret.add(tuple(subset[:])) #[:] saves time vs arr.copy()
                return
            if sum > target or i == len(candidates):    return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                subset.append(candidates[j])
                helper(j+1, sum+candidates[j])
                subset.pop()

        helper(0, 0)
        return ret
