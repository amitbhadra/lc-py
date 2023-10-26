class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l, r = 0, 1
        maxSubsLen = 1
        maxSubs = set(s[0]) # set stores uniq characters
        subs = {s[0]: 0} # store char: index
        while r < len(s):
            if s[r] not in maxSubs:
                subs[s[r]] = r
                maxSubs.add(s[r])
                maxSubsLen = max(maxSubsLen, len(maxSubs))
            else:
                # pop elements from l to last occurance of s[r]
                for i in range(l, subs[s[r]]):
                    subs.pop(s[i])
                    maxSubs.remove(s[i])
                # then update l to last occurance of s[r] + 1
                l = subs[s[r]] + 1
                subs[s[r]] = r
            r += 1
        return maxSubsLen
