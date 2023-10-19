class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures))[::-1]:
            t = temperatures[i]
            # only store the largest values
            while stack and stack[-1][0] <= t:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            else:
                res[i] = 0
            stack.append([t, i])
        return res
