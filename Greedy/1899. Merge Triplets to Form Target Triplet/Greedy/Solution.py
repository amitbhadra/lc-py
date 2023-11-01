# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tripletIndices = set()

        for triplet in triplets:
            if any(triplet[i] > target[i] for i in range(len(target))): continue
            for i, val in enumerate(triplet):
                if val == target[i]:
                    tripletIndices.add(i)

        return len(tripletIndices) == len(target)
