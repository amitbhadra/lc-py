# https://leetcode.com/problems/length-of-the-longest-valid-substring/description/
# THIS SHOULD NOT BE SOLVED BY DP, IT GETS TLE. SOLVE USING HASHMAPS
# BUT THE SOLUTION IS CORRECT

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbiddenSet = set(forbidden)
        dp = [[False] * (len(word)+1) for i in range(len(word)+1)]

        maxLen = 0
        for i in range(len(word)):
            if word[i] not in forbiddenSet:
                dp[i][i] = True
                maxLen = 1

        for size in range(1, len(word)):
            for idx in range(len(word) - size):
                i, j = idx, idx+size
                substr = word[i:j+1]
                if dp[i][j-1] and dp[i+1][j] and substr not in forbiddenSet:
                    dp[i][j] = True
                    maxLen = max(size+1, maxLen)

        return maxLen
