# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1 
        sentinel = ListNode(-1)
        dummyHead = sentinel
        carry=0
        while l1 or l2:
            x,y=0,0
            if l1 is not None:
                x=l1.val
                l1=l1.next
            if l2 is not None:
                y=l2.val
                l2=l2.next
            sum = x+y+carry
            digit = sum%10 if sum > 9 else sum
            carry =  sum//10 if sum >9 else 0
            dummyHead.next= ListNode(digit)
            dummyHead=dummyHead.next
        if carry >0:
            dummyHead.next= ListNode(carry)
        return sentinel.next

    
        