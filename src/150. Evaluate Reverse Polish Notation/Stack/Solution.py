class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in ['+', '-', '/', '*']:
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                if c == '+':
                    res = a + b
                elif c == '-':
                    res = a - b
                elif c == '*':
                    res = a * b
                else:
                    res = int(a / b)
                stack.append(res)

        return stack.pop()
