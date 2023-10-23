class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:   return True
        adj_matrix = [[0] * numCourses for r in range(numCourses)]
        for r, c in prerequisites:
            if r == c:  return False
            adj_matrix[c][r] = 1

        visited = set()
        def traverse(r):
            if r in visited:  return True
            if r in tmp_path:  return False
            tmp_path.append(r)
            for c in range(numCourses):
                if adj_matrix[r][c] == 1:
                    if not traverse(c):
                        return False
            tmp_path.pop()
            visited.add(r)
            return True

        for r in range(numCourses):
            for c in range(numCourses):
                if adj_matrix[r][c] == 1 and c not in visited:
                    tmp_path = [r]
                    if not traverse(c):  return False

        return True
