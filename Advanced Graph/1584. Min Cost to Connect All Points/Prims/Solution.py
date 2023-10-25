# Prim's
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjList = { n: [] for n in range(N) } # {src: [weight, dest]}

        # create Adj list
        for i in range(N):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i, N):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])

        # Prim's
        res = 0 # cost of MST
        minHeap = [[0, 0]] # start from 0th point
        visited = set()
        while len(visited) != N:
            dist1, p1 = heapq.heappop(minHeap)
            if p1 in visited:   continue
            visited.add(p1)
            res += dist1
            for dist2, p2 in adjList[p1]:
                if p2 not in visited:
                    heapq.heappush(minHeap, [dist2, p2])

        return res
