class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        leftCandle = [0 if s[0] == '|' else -1] # stores candle to the left index
        prefixSum = [1 if s[0] == '*' else 0] # sums of all plates
        idx = 1
        for c in s[1:]:
            prefixSum.append(prefixSum[-1] + (1 if c == '*' else 0))
            leftCandle.append(idx if c == '|' else leftCandle[-1])
            idx += 1
        # print(len(s))
        # print(prefixSum)
        # print(leftCandle)

        rightCandle = collections.deque()
        rightCandle.append(len(s)-1 if s[len(s)-1] == '|' else -1) # stores candle to the right index
        idx = len(s) - 2
        for c in s[-2::-1]: # list from end index - 1 to 0 ie, in reverse order
            rightCandle.appendleft(idx if c == '|' else rightCandle[0])
            idx -= 1
        # print(rightCandle)

        res = []
        for start, end in queries:
            # left will be the right candle index of start
            # right will be the left candle index of end
            left = rightCandle[start]
            right = leftCandle[end]
            # print(left, right)
            # 0 if left > right when there are no candles between
            # Eg: "*|*|||" and [0,0]
            res.append(0 if left > right else max(prefixSum[right] - prefixSum[left], 0))

        return res
