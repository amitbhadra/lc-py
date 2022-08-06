class Solution:
    def traversal(self, i, adj, visited, visited_in_traversal):
        if visited_in_traversal[i] or visited[i]:
            return False
        
        visited_in_traversal[i] = True
        for node in adj[i]:
            self.traversal(node, adj, visited, visited_in_traversal)
        
        visited[i] = True
        return visited[i]
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        islands = 0
        from collections import defaultdict
        adj = defaultdict(list)
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        for i in range(n):
            visited_in_traversal = [False] * n
            if self.traversal(i, adj, visited, visited_in_traversal):
                islands += 1
        
        return islands

# Better than 35% of the solutions
