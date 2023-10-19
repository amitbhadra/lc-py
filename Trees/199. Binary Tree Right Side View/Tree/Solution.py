# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:    return ret
        queue = [root]

        while queue:
            queueLen = len(queue)
            ret.append(queue[-1].val)
            for i in range(queueLen):
                node = queue.pop(0)
                if node:
                    if node.left:   queue.append(node.left)
                    if node.right:   queue.append(node.right)

        return ret


# DFS
class Solution:
    # The plan here is to dfs the tree, right-first
    # (opposite of  the usual left-first method), and
    # keeping track of the tree levels as we proceed. The 
    # first node we visit on each level is the right-side view 
    # node. We know it's the first because the level will be
    # one greater than the length of the current answer list.
    def rightSideView(self, root: TreeNode) -> list[int]:
        ans =[]     
        def dfs(node =root,level=1):
            if not node: return
            if len(ans) < level: 
                ans.append(node.val)
            dfs(node.right,level+1)         #  <--- right first
            dfs(node.left ,level+1)         #  <--- then left
            return 
        dfs()
        return ans
