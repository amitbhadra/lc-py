class Solution:
    def numDecodings(self, s):

        dp = [-1] * (len(s)+1)
        dp[len(s)] = 1

        def dfs(i):

            if dp[i] != -1:
                return dp[i]
			
			# We can do this if we dont assign dp[len(s)] = 1
            # if i == len(s):
            #     return 1

            if s[i] == "0":
                return 0

            ans = dfs(i+1)

            if i + 1 < len(s) and 0 < int(s[i:i+2]) < 27:
                ans += dfs(i+2)

            dp[i] = ans

            return ans
        return dfs(0)
