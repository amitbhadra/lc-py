class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return heights
        rows, cols = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []

        def isPac(r, c):
            if r < 0 or c < 0:  return True
            return False
        
        def isAtl(r, c):
            if r == rows or c == cols:  return True
            return False

        def traverse(r, c):
            queue = [[r, c]]
            Pac = Atl = False
            while queue:
                r, c = queue.pop()
                if (r, c) in visited:   continue
                visited.add((r, c))
                for d in directions:
                    newR, newC = r+d[0], c+d[1]
                    Pac = isPac(newR, newC) or Pac
                    Atl = isAtl(newR, newC) or Atl
                    if Pac and Atl: return Pac, Atl
                    condition = (
                        newR >= 0 and newR < rows and
                        newC >= 0 and newC < cols and
                        (newR, newC) not in visited and
                        heights[r][c] >= heights[newR][newC]
                    )
                    if condition:   queue.append((newR, newC))
            return Pac, Atl

        for r in range(rows):
            for c in range(cols):
                visited = set()
                Pac, Atl = traverse(r, c)
                if Pac and Atl:
                    res.append([r, c])

        return res
