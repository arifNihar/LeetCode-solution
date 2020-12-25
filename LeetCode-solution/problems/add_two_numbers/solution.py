# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = i = 0
        new_node = prev = None

        while l1 or l2:
            if l1 is None:
                data = (l2.val + c)%10
                c = (l2.val + c)//10
                l2 = l2.next
                
            elif l2 is None:
                data = (l1.val + c)%10
                c = (l1.val + c)//10
                l1 = l1.next
            else:
                data = (l1.val + l2.val + c)%10
                c = (l1.val + l2.val + c)//10
                l1 = l1.next
                l2 = l2.next
            new_node = ListNode(data)
            if i == 0:
                head = new_node
            else:
                prev.next = new_node

            prev = new_node
            if c:
                new_node.next = ListNode(c)
            i += 1
        return head
            