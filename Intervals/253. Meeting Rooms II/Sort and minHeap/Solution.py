# https://leetcode.com/problems/meeting-rooms-ii/description/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:   return 0
        intervals.sort(key = lambda x: x[0])
        maxRooms = 1
        minHeap = [intervals[0][1]]

        for start, end in intervals[1:]:
            while minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
            maxRooms = max(len(minHeap), maxRooms)

        return maxRooms
