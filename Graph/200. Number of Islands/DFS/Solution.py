class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:    return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def traverse(r, c):
            queue = [[r, c]]
            while queue:
                pos_r, pos_c = queue.pop()
                visited.add((pos_r, pos_c))
                for d in directions:
                    new_r, new_c = pos_r + d[0], pos_c + d[1]
                    valid = (
                        new_r >= 0 and new_r < rows and
                        new_c >= 0 and new_c < cols and
                        grid[new_r][new_c] == '1' and
                        (new_r, new_c) not in visited
                    )
                    if not valid:   continue
                    queue.append([new_r, new_c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    traverse(r, c)
                    islands += 1

        return islands
