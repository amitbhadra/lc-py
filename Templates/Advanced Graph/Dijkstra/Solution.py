# Gets TLE for https://leetcode.com/problems/cheapest-flights-within-k-stops/

# Dijkstra
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create Adj List
        adjList = collections.defaultdict(list)
        for flight in flights:
            adjList[flight[0]].append([flight[2], flight[1]]) # {src: [cost, dest]}

        # Dijkstra (uses BFS)
        minHeap = [[0, -1, src]] #[cost, dist, airport]
        # minCostHash = {} #[cost]

        while minHeap:
            cost1, dist1, airport1 = heapq.heappop(minHeap)
            if dist1 > k:   continue
            # This is Dijkstra guarantee
            if airport1 == dst: return cost1

            # if airport1 in minCostHash:
            #     if cost1 < minCostHash[airport1]:
            #         minCostHash[airport1] = cost1
            # else:
            #     minCostHash[airport1] = cost1

            if dist1 + 1 <= k:
                for cost, nei in adjList[airport1]:
                    heapq.heappush(minHeap, [cost+cost1, dist1+1, nei])
        return -1
        return minCostHash[dst] if dst in minCostHash else -1
