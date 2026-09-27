# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 0 1 2 3 4 5 6 

        # 0 1 2 6 5 4 3

        # 0 6 1 5 2 4 3 

        #we need to find middle with fast and slow pointer
        #reverse second half of linked list 
        #alternate between first and new order second half with a pointer

        #find middle

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        print(slow.val)

        prev = None
        curr = slow.next
        slow.next = None

        #reverse second half
        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        #iterate through both halves alternating 
        first, second = head, prev
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2




        