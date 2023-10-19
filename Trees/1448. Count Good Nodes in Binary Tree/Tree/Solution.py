# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:    return 0
        def helper(node, maxNodeVal):
            if not node:    return 0
            goodNodes = 0
            if node.val >= maxNodeVal: goodNodes += 1
            return goodNodes + helper(node.left, max(maxNodeVal, node.val)) + helper(node.right, max(maxNodeVal, node.val))
        return helper(root, root.val)
