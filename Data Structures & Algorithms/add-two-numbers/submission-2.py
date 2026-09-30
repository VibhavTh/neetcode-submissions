# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        h1, h2 = l1, l2
        res = ListNode(0, None)
        h3 = res

        sum = h1.val + h2.val
        carry = 0
        if sum >= 10:
            carry = 1
        
        res.val = sum % 10
        h1, h2 = l1.next, l2.next

        while h1 or h2 or carry:
            v1 = h1.val if h1 else 0
            v2 = h2.val if h2 else 0
            sum = v1 + v2 + carry
            carry = 0



            if sum >= 10:
                carry = 1
                sum = sum % 10

            newNode = ListNode(sum, None)
            res.next = newNode
            res = res.next
            if h1:
                h1 = h1.next
            
            if h2:
                h2 = h2.next
        

        return h3
            
            





        