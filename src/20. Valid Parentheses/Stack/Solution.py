class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if not stack:
                    return False
                last = stack.pop()
                if valid[last] != c:
                    return False
        if stack:
            return False
        return True
