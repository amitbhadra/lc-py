# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        allNodes = []
        if not root:   return allNodes
        queue = [root]
        while queue:
            queueLen = len(queue)
            allNodes.append([n.val for n in queue])
            for i in range(queueLen):
                node = queue.pop(0)
                if node:
                    if node.left:   queue.append(node.left)
                    if node.right:   queue.append(node.right)
        return allNodes
