# https://leetcode.com/problems/longest-common-subsequence/description/
# Time Complexity: O(N*M)
# Space Complexity: O(N*M) + O(N+M)

def f(ind1,ind2,s1,s2,dp):
	if(ind1<0 or ind2<0):
		return 0
	
	if(dp[ind1][ind2] != -1):
		return dp[ind1][ind2]
	
	if(s1[ind1] == s2[ind2]):
		dp[ind1][ind2] = 1 + f(ind1-1,ind2-1,s1,s2,dp)
		return dp[ind1][ind2]
	
	dp[ind1][ind2] = max(f(ind1-1,ind2,s1,s2,dp),f(ind1,ind2-1,s1,s2,dp))
	return dp[ind1][ind2]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for i in range(len(text2))] for i in range(len(text1))]
        return f(n-1,m-1,text1,text2,dp)
