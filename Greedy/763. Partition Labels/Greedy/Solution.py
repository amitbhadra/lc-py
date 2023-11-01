# https://leetcode.com/problems/partition-labels/description/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastCharIdx = {}
        for i in range(len(s)):
            lastCharIdx[s[i]] = i

        res = []
        lastIdx = 0
        maxIdx = -1
        for i in range(len(s)):
            maxIdx = max(maxIdx, lastCharIdx[s[i]])
            if i == maxIdx:
                res.append(i - lastIdx + 1)
                lastIdx = i + 1

        return res
