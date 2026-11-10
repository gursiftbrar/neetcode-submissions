# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        carry = 0 

        p1 = l1
        p2 = l2

        dummy = ListNode(0) # starts us off with 0
        current = dummy 

        while p1 is not None or p2 is not None or carry == 1:
            val1 = p1.val if p1 is not None else 0
            val2 = p2.val if p2 is not None else 0

            total = val1 + val2 + carry

            digit = total % 10 # gives ones place
            carry = total // 10 # carries tens place

            new_node = ListNode(digit)

            current.next = new_node 
            current = current.next # moves current from 0 to next in like list

            if p1 is not None:
                p1 = p1.next

            if p2 is not None:
                p2 = p2.next
            
        return dummy.next # head of the completed result

 
            