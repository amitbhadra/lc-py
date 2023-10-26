class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        charMap1, charMap2 = {}, {}
        for c in range(ord('a'), ord('z')+1):
            charMap1[chr(c)] = charMap2[chr(c)] = 0
        for i in range(len(s1)):
            charMap1[s1[i]] += 1
            charMap2[s2[i]] += 1
        
        for i in range(len(s1), len(s2)):
            if charMap1 == charMap2:
                return True
            charMap2[s2[i - len(s1)]] -= 1
            charMap2[s2[i]] += 1

        return charMap1 == charMap2 
