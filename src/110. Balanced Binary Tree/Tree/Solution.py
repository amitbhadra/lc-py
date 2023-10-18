# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def helper(node):
            if not node:    return 0
            left = helper(node.left)
            right = helper(node.right)
            if abs(left - right) in [0, 1]:
                self.balanced = self.balanced and True
            else:
                self.balanced = False
            return (max(left, right) + 1)
        _ = helper(root)
        return self.balanced
