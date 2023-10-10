# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        headL1, headL2 = l1, l2
        carry = 0

        Res = ListNode()
        node = Res
        while headL1 or headL2:
            sum = carry
            if headL1:
                sum += headL1.val
                headL1 = headL1.next
            if headL2:
                sum += headL2.val
                headL2 = headL2.next

            if sum >= 10:
                sum -= 10
                carry = 1
            else:
                carry = 0
            Node = ListNode(sum)
            node.next = Node
            node = Node

        if carry:
            node.next = ListNode(1)

        return Res.next
