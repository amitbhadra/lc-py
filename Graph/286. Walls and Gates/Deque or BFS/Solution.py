class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:   return
        rows, cols = len(rooms), len(rooms[0])
        
        # find gates
        gates = collections.deque()
        num_rooms = 0
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:    gates.append((r, c))
                elif rooms[r][c] != -1: num_rooms += 1

        # traverse from gate outwards
        visited = set()
        num_steps = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while gates:
            lenGates = len(gates)
            num_steps += 1
            for i in range(lenGates):
                r, c = gates.popleft()
                if (r, c) in visited:   continue
                visited.add((r, c))
                for d in directions:
                    newR, newC = r + d[0], c + d[1]
                    condition = (
                        newR >= 0 and newR < rows and
                        newC >= 0 and newC < cols and
                        (newR, newC) not in visited and
                        rooms[newR][newC] > num_steps
                    )
                    if condition:
                        rooms[newR][newC] = num_steps
                        gates.append((newR, newC))
        
        return
