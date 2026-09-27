# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        fast, slow = head, dummy
        prev = None

        #move fast pointer slow + n steps to start then iterate till fast == None
        #use a dummy pointer to avoid special case to remove head


        for x in range(n):
            fast = fast.next
        
    
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next



