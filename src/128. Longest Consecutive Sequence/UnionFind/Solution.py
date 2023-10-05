class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        class Node:
            def __init__(self, val):
                self.val = val
                self.parent = self
                self.length = 1
        
        class UF:
            def __init__(self):
                self.nodes = {}

            def find_parent(self, node):
                parent = node.parent
                if node.parent != node:
                    parent = self.find_parent(node.parent)
                # path compression
                node.parent = parent
                return parent

            def join(self, node1, node2):
                parent1 = self.find_parent(node1)
                parent2 = self.find_parent(node2)
                length = parent1.length
                if parent1 != parent2:
                    # optimization
                    if parent1.length > parent2.length:
                        parent2.parent = parent1
                        parent1.length += parent2.length
                        length = parent1.length
                    else:
                        parent1.parent = parent2
                        parent2.length += parent1.length
                        length = parent2.length
                return length


        uf = UF()
        for n in nums:
            if n not in uf.nodes:
                uf.nodes[n] = Node(n)
        max_length = 0
        for n, node in uf.nodes.items():
            length = 1
            if n-1 in uf.nodes:
                length = uf.join(uf.nodes[n], uf.nodes[n-1])
            if n+1 in uf.nodes:
                length = uf.join(uf.nodes[n], uf.nodes[n+1])
            max_length = max(length, max_length)
        return max_length
