class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1, n2 = len(str1), len(str2)
        idx2, i = 0, 0
        
        while i < n2:
            oldIdx2 = idx2
            for idx1 in range(i, n1):
                newChar = chr(ord(str1[idx1]) + 1) if str1[idx1] != 'z' else 'a'
                if str2[idx2] == str1[idx1] or str2[idx2] == newChar:
                    idx2 += 1
                    i = idx1 + 1
                    if idx2 == n2:    return True
            if oldIdx2 == idx2: return False

        return
