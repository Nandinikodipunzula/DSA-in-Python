# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPtr = head
        fastPtr = head
        while fastPtr and fastPtr.next :
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if fastPtr == slowPtr:
                return True
        return False


def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  
    
    solution = Solution()
    has_cycle = solution.hasCycle(node1)
    print("Does the linked list have a cycle?", has_cycle)

if __name__ == "__main__":
    main()
