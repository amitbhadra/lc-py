class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i:i[0])
        last_start, last_end = intervals[0]
        for start, end in intervals[1:]:
            if start < last_end:
                return False
            last_start = start
            last_end = end
        return True
