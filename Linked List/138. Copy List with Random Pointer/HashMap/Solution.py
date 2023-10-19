"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        nodeMap = {} # old: new

        # traverse next ptr
        node = head
        newHead = Node(node.val)
        prev = newHead
        nodeMap[node] = newHead

        node = node.next
        while node:
            newNode = Node(node.val)
            if prev: prev.next = newNode
            nodeMap[node] = newNode
            prev = newNode
            node = node.next

        # traverse random ptr
        node = head
        while node:
            deepNode = nodeMap.get(node, None)
            if deepNode:
                randomNode = nodeMap.get(node.random, None)
                deepNode.random = randomNode
            node = node.next

        return newHead
