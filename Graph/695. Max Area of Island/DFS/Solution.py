class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:    return 0
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def findArea(r, c):
            queue = [[r, c]]
            area = 0
            while queue:
                curR, curC = queue.pop()
                if (curR, curC) in visited: continue
                visited.add((curR, curC))
                area += 1
                for d in directions:
                    newR, newC = curR + d[0], curC + d[1]
                    condition = (
                        newR >= 0 and newR < rows and
                        newC >= 0 and newC < cols and
                        grid[newR][newC] == 1 and
                        (newR, newC) not in visited
                    )
                    if condition:
                        queue.append((newR, newC))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, findArea(r, c))
        return maxArea
