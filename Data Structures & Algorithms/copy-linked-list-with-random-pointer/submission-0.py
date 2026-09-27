"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':



        # Maps each original node to its new copied node.
        # Mapping None to None simplifies pointer assignments.
        info = {None: None}

        # First pass: create all copied nodes.
        curr = head
        while curr:
            info[curr] = Node(curr.val)
            curr = curr.next

       # Second pass: connect next and random pointers.
        curr = head
        while curr:
            copy = info[curr]
            copy.next = info[curr.next]
            copy.random = info[curr.random]
        
            curr = curr.next

        
        return info[head]
