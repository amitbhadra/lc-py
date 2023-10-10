# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            def removeN(head, n):
                if head is None:
                    return [head, n]
                nxt, N = removeN(head.next, n)
                if N == 1:
                    return [head.next, N-1]
                else:  
                    head.next = nxt
                    return [head, N-1]

            return removeN(head, n)[0]
