# https://leetcode.com/problems/minimum-interval-to-include-each-query/

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        res = {}
        minHeap = []
        i = 0

        for query in sorted(queries):
            
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            res[query] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
