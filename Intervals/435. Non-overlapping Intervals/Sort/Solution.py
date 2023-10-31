# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if not intervals:   return res
        # we sort by end index because we don't need to keep all the intervals
        intervals.sort(key = lambda x: x[1])

        start, end = intervals[0]
        i = 1
        while i < len(intervals):
            newInterval = intervals[i]
            if newInterval[0] < end:
                res += 1
            else:
                start, end = newInterval
            i += 1
        return res
