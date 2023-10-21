class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:   return
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # find borders
        borders = []
        def findBorders():
            for r in range(rows):
                borders.append([r, 0])
                borders.append([r, cols-1])
            for c in range(cols):
                borders.append([0, c])
                borders.append([rows-1, c])
        findBorders()

        # mark all non-surrounded 'O's as 'E'
        def traverse(r, c):
            queue = [[r, c]]
            while queue:
                r, c = queue.pop()
                if (r, c) in visited:   continue
                visited.add((r, c))
                board[r][c] = 'E'
                for d in directions:
                    newR, newC = r + d[0], c + d[1]
                    condition = (
                        newR > 0 and newR < rows-1 and
                        newC > 0 and newC < cols-1 and
                        board[newR][newC] == 'O' and
                        (newR, newC) not in visited
                    )
                    if condition:   queue.append([newR, newC])

        # traverse inwards from the borders
        for b in borders:
            r, c = b[0], b[1]
            if board[r][c] == 'O':
                visited = set()
                traverse(r, c)

        # mark all non surrounded 'O's as 'X' and mark all
        # 'E's as 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'E':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

        return        
