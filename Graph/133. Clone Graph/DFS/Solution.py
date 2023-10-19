"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:    return node
        newRoot = Node(1)

        nodes = {1: newRoot}
        queue = [node]
        visited = set()

        while queue:
            item = queue.pop()
            # check if node has been visited
            if item.val in visited: continue
            visited.add(item.val)

            # create the node if not
            if item.val not in nodes:
                deepItem = Node(item.val)
                nodes[item.val] = deepItem
            else:
                deepItem = nodes[item.val]

            # traverse neighbors
            for neighbor in item.neighbors:
                if neighbor.val not in nodes:
                    deepNeighbor = Node(neighbor.val)
                    nodes[neighbor.val] = deepNeighbor
                else:
                    deepNeighbor = nodes[neighbor.val]
                queue.append(neighbor)
                deepNeighbor.neighbors.append(deepItem)
                #deepItem.neighbors.append(deepNeighbor)

        return newRoot
