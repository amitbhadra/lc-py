class Node:
    def __init__(self, val, parent=None, rank=1):
        self.val = val
        self.parent = self
        self.rank = rank

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = {}

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
                return True
            else:
                # path compression
                if parentR.rank > parentC.rank:
                    parentC.parent = parentR
                    parentR.rank += parentC.rank
                else:
                    parentR.parent = parentC
                    parentC.rank += parentR.rank
            return False

        for edge in edges:
            r, c = edge[0], edge[1]
            if union(r, c): return r, c
        return
