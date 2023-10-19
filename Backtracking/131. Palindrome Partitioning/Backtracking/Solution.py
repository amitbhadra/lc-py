class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        part = []

        def helper(i):
            if i == len(s):
                ret.append(part[:])
                return
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    part.append(s[i:j+1])
                    helper(j+1)
                    part.pop()

        helper(0)
        return ret
