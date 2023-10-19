# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

# Recursive
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root:
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root

# Non BST solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.answer = TreeNode('x')
        def helper(node):
            if not node:    return [False, False]
            ret = [False, False]
            if node.val == p.val:
                ret = [True, False]
            elif node.val == q.val:
                ret = [False, True]
            retLeft = helper(node.left)
            retRight = helper(node.right)
            ret = [ret[0] or retLeft[0] or retRight[0], ret[1] or retLeft[1] or retRight[1]]
            if ret == [True, True] and self.answer.val == 'x':
                self.answer = node
            return ret

        _ = helper(root)
        return self.answer
