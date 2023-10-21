class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:    return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # find rotten oranges
        rotten = collections.deque()
        num_fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: rotten.append((r, c))
                elif grid[r][c] == 1:   num_fresh += 1
        if num_fresh == 0:  return 0

        visited = set()
        num_mins = 0
        while rotten:
            items = len(rotten)
            for item in range(items):
                r, c = rotten.popleft()
                if (r, c) in visited:   continue
                visited.add((r, c))
                if grid[r][c] == 1: num_fresh -= 1
                if num_fresh == 0:  return num_mins
                for d in directions:
                    newR, newC = r + d[0], c + d[1]
                    condition = (
                        newR >= 0 and newR < rows and
                        newC >= 0 and newC < cols and
                        (newR, newC) not in visited and
                        grid[newR][newC] != 0
                    )
                    if condition:   rotten.append((newR, newC))
            num_mins += 1
        return -1
