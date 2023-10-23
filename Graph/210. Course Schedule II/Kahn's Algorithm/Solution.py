# Kahn's algorithm
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adjMatrix = {n: [] for n in range(numCourses)}

        # create AdjMatrix
        for r, c in prerequisites:
            adjMatrix[c].append(r)
            indegrees[r] += 1

        # create indegrees
        queue = collections.deque()
        for i in range(numCourses):
            if indegrees[i] == 0:   queue.append(i)

        # traverse based on indegrees
        res = []
        nodesVisited = 0
        while queue:
            node = queue.popleft()
            res.append(node)
            nodesVisited += 1
            for neighbor in adjMatrix[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0: queue.append(neighbor)

        return res if nodesVisited == numCourses else []
