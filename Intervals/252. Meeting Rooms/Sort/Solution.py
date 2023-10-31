# https://leetcode.com/problems/meeting-rooms/description/

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:   return True
        intervals.sort(key = lambda x: x[0])
        prev = -math.inf
        for start, end in intervals:
            if start < prev:    return False
            prev = end
        return True
