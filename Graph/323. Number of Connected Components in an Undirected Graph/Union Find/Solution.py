# Union Find
class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def findParent(node):
            if node.parent != node:
                node.parent = findParent(node.parent)
            return node.parent

        def union(r, c):
            if r not in nodes:  nodes[r] = Node(r)
            if c not in nodes:  nodes[c] = Node(c)
            parentR = findParent(nodes[r])
            parentC = findParent(nodes[c])
            if parentR != parentC:
                if parentR.rank > parentC.rank:
                    parentC.parent = parentR
                    parentR.rank += parentC.rank
                else:
                    parentR.parent = parentC
                    parentC.rank += parentR.rank
        
        # add to unionFind DS
        nodes = {}
        for i, j in edges:
            union(i, j)
        
        # check how many parents exist
        res = 0
        for i in range(n):
            if i not in nodes:  res += 1
            elif nodes[i].parent == nodes[i]:   res += 1

        return res
