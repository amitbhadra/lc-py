class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        op = ''
        for s in strs:
            op += str(len(s)) + '#' + s
        return op

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        op = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            nums = int(s[i: j])
            op.append(s[j+1: j+1+nums])
            i = j+1+nums
        return op


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))