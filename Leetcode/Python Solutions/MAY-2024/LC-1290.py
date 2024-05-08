class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return 0
        nodePtr = head
        numStr=''
        while nodePtr:
            numStr+= str(nodePtr.val)
            nodePtr=nodePtr.next
        k=0
        ans = 0
        for i in range(len(numStr)-1,-1,-1):
            ans+=int(numStr[i])*pow(2,k)
            k+=1
        return ans


        