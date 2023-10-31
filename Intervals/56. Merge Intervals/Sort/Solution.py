# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:   return intervals
        intervals.sort(key= lambda x:x[0]) # optimization over default intervals.sort()
        res = []
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            newInterval = intervals[i]
            if newInterval[0] <= end:
                end = max(end, newInterval[1])
            else:
                res.append([start, end])
                start, end = newInterval
        res.append([start, end])
        return res
