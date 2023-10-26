class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left, self.right = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.start = Node(-1, -1)
        self.end = Node(-1, -1)
        self.start.right = self.end
        self.end.left = self.start

    def updateNodePosition(self, node):
        nodeLeft, nodeRight = node.left, node.right
        if node.left:   node.left.right = nodeRight
        if node.right:  node.right.left = nodeLeft
        lastNode = self.end.left
        lastNode.right = node
        node.left = lastNode
        node.right = self.end
        self.end.left = node

    def get(self, key: int) -> int:
        #print('get', key)
        if key not in self.map: return -1
        node = self.map[key]
        self.updateNodePosition(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        #print('put', key)
        if key in self.map:
            node = self.map[key]
            node.val = value
        else:
            if len(self.map) == self.capacity:
                leastUsedNode = self.start.right
                self.map.pop(leastUsedNode.key)
                self.start.right = leastUsedNode.right
                if leastUsedNode.right: leastUsedNode.right.left = self.start
            node = Node(key, value)
            self.map[key] = node
        self.updateNodePosition(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
