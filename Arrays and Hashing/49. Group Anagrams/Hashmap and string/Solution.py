import collections
import string


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_map():
            charmap = {}
            for c in list(string.ascii_letters[:26]):
                charmap[c] = 0
            return charmap
        def get_key(s):
            charmap = get_map()
            for c in s:
                charmap[c] += 1
            key = ''
            for c in list(string.ascii_letters[:26]):
                if charmap[c]:
                    key = key + c + str(charmap[c])
            return key

        wordmap = collections.defaultdict(list)
        for s in strs:
            key = get_key(s)
            print(key)
            wordmap[key].append(s)
        return wordmap.values()
