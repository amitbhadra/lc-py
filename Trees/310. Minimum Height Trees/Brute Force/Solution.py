class Solution:
    def findHeight(self, i, n, adj):
        height = 0
        queue = [i]
        visited = [False] * n
        while queue:
            queueSize = len(queue)
            for j in range(queueSize):
                node = queue.pop(0)
                if not visited[node]:
                    visited[node] = True
                    for k in adj[node]:
                        queue.append(k)
            height += 1
        return height
            
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        minHeight = n + 1
        minHeightList = []
        
        for i in range(n):
            height = self.findHeight(i, n, adj)
            if height < minHeight:
                minHeight = height
                minHeightList = [i]
            elif height == minHeight:
                minHeightList.append(i)
        
        return minHeightList

# TC: O(n^2) this results in Time exceeded
