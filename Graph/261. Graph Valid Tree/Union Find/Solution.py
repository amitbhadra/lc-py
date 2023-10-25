class Node:
    def __init__(self, val, parent=None, rank=1):
        self.val = val
        self.parent = self
        self.rank = rank

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {}

        # optimization and edge
        if n != len(edges) + 1: return False
        if n == 1 and len(edges) == 0:  return True

        def getParent(nodeR):
            if nodeR.parent != nodeR:
                nodeR.parent = getParent(nodeR.parent)
            return nodeR.parent

        def union(r, c):
            if r not in nodes:  nodes[r] = Node(r)
            if c not in nodes:  nodes[c] = Node(c)
            parentR = getParent(nodes[r])
            parentC = getParent(nodes[c])
            if parentR == parentC:
                return False
            else:
                # path compression
                if parentR.rank > parentC.rank:
                    parentC.parent = parentR
                    parentR.rank += parentC.rank
                else:
                    parentR.parent = parentC
                    parentC.rank += parentR.rank
            return True

        for edge in edges:
            r, c = edge[0], edge[1]
            if not union(r, c): return False

        numParents = 0
        for i in range(n):
            if i not in nodes:  return False
            elif nodes[i].parent == nodes[i]:
                numParents += 1
                if numParents > 1:  return False
        return True
