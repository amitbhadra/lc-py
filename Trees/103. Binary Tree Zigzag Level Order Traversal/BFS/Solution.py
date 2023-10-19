# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        l2r = True
        output = []

        def get_nodes(arr, order_l2r=True):
            arr_int = [n.val for n in arr]
            if not l2r:
                arr_int.reverse()
            return arr_int
    
        while queue:
            output.append(get_nodes(queue, l2r))
            l2r = not l2r
            num = len(queue)
            for i in range(num):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return output
