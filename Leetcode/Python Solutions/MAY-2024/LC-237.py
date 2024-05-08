# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#overwrite the value of the node to be deleted with next node val
#and point the node to node.next.next
#Note: Read the editorial, this question editorial is free and it is has beautiful explanation
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
        