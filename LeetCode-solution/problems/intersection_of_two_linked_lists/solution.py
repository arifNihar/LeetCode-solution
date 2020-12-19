# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr1, curr2 = headA, headB
        while curr1 != curr2:
            if curr1 is None:
                curr1 = headB
            else:
                curr1 = curr1.next
            if curr2 is None:
                curr2 = headA
            else:
                curr2 = curr2.next 
        return curr1
        