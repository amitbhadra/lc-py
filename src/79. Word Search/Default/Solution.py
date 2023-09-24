# ## Testcases
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCCED"

# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "SEE"

# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCB"

# [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# "ABCESEEEFS"

# [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
# "AAAAAAAAAAAAAAB"

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def up(r, c):
            if r == 0:
                return False
            return (r-1, c)

        def down(r, c):
            if r >= len(board)-1:
                return False
            return (r+1, c)

        def left(r, c):
            if c == 0:
                return False
            return (r, c-1)

        def right(r, c):
            if c >= len(board[0])-1:
                return False
            return (r, c+1)

        def search(r, c, visited, idx):
            if visited[r][c]:
                return False
            if idx == len(word)-1:
                return True
            visited[r][c] = True
            if up(r, c):
                new_r, new_c = up(r, c)
                if board[new_r][new_c] == word[idx+1] and search(new_r, new_c, visited, idx+1):
                    return True
            if down(r, c):
                new_r, new_c = down(r, c)
                if board[new_r][new_c] == word[idx+1] and search(new_r, new_c, visited, idx+1):
                    return True
            if left(r, c):
                new_r, new_c = left(r, c)
                if board[new_r][new_c] == word[idx+1] and search(new_r, new_c, visited, idx+1):
                    return True
            if right(r, c):
                new_r, new_c = right(r, c)
                if board[new_r][new_c] == word[idx+1] and search(new_r, new_c, visited, idx+1):
                    return True
            visited[r][c] = False
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                    if search(r, c, visited, 0):
                        return True
        return False
