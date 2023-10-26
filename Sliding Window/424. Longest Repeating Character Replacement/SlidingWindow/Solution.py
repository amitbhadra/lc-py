class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # move from l to r and check if the number of characters
        # which is not the max character is <= k
        l, r = 0, 0
        charCount = {}
        maxLen = 0
        while r < len(s):
            count = charCount.get(s[r], 0) + 1
            charCount[s[r]] = count
            maxCount = max(charCount.values())
            if r - l + 1 - maxCount <= k:
                maxLen = max(maxLen, r - l + 1)
            else:
                charCount[s[l]] -= 1
                l += 1
            r += 1

        return maxLen
