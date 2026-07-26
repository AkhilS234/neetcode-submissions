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

        result = []
        oldToCopy = {None:None}
        ptr = head

        while (ptr is not None):
            newNode = Node(x=ptr.val, next=None)
            oldToCopy[ptr] = newNode
            ptr = ptr.next

        curr = head
        while (curr is not None):
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]

        


    