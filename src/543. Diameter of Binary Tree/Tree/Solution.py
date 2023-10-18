# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0
        def helper(node):
            if not node:    return 0
            left = helper(node.left)
            right = helper(node.right)
            self.maxDiam = max(self.maxDiam, left, right, left + right)
            return max(left + 1, right + 1)

        _ = helper(root)
        return self.maxDiam
