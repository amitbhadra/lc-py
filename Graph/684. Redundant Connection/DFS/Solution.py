class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        adjMatrix = {i:[] for i in range(len(edges)+1)}

        def isConnected(i, j):
            if i in temp_path:   return False
            if i == j:  return True
            temp_path.append(i)
            for neighbor in adjMatrix[i]:
                if isConnected(neighbor, j):
                    return True

        for i, j in edges:
            temp_path = []
            if i in visited and j in visited and isConnected(i, j):
                return [i, j]
            adjMatrix[i].append(j)
            adjMatrix[j].append(i)
            visited.add(i)
            visited.add(j)
        return
