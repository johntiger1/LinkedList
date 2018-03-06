# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return head
        
        curr = head
        prev = None
        
        while (curr is not None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
        