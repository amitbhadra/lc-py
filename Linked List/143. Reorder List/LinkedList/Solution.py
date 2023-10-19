# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        stack = []
        saved_head = head
        while head:
            stack.append(head)
            head = head.next

        head = saved_head
        for i in range(len(stack)//2):
            n=stack.pop()
            t=head.next
            head.next=n
            n.next=t
            head=t
        head.next=None
