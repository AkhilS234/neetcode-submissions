# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2
        output = []
        num1 = ''
        num2 = ''
        new = ListNode()
        dummy = new
        carry = 0

        while ((p1 is not None) or (p2 is not None)):
            if p1:
                val1 = p1.val 
            else: 
                val1 = 0
            if p2:
                val2 = p2.val
            else:
                val2 = 0
            currSum = val1 + val2 + carry
            
            if (currSum > 9):
                curr = currSum - 10
                carry = 1
                new.next = ListNode(curr)
                new = new.next
            else: 
                new.next = ListNode(currSum)
                new = new.next
                carry = 0
            
            if (p1 is not None):
                p1 = p1.next
            if (p2 is not None):
                p2 = p2.next
        if (carry > 0):
                new.next = ListNode(carry)
                new = new.next
        return dummy.next

