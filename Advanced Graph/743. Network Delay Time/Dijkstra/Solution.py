# Dijkstra
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for src, dst, time in times:
            adjList[src].append([time, dst])

        visited = set()
        maxTimeSoFar = 0
        minHeap = [[0, k]] #[time, node]
        while minHeap:
            time, node = heappop(minHeap)
            if node in visited: continue
            visited.add(node)
            maxTimeSoFar = max(maxTimeSoFar, time)
            if len(visited) == n:   break
            for newTime, nei in adjList[node]:
                heappush(minHeap, [time + newTime, nei])

        return maxTimeSoFar if len(visited) == n else -1
