"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    
    # base case:
    if head is None:
        return head
    # a couple of solutions:
    # connect each one as it "comes"
    
    prev = None
    curr = head
    next = head.next
    
    while (curr is not None):
        curr.next = prev
        prev=curr
        curr = next
        if next is None:
            return prev
        next = next.next
    
    # at the end, curr is None
    return prev
    
    
    
  
  
  
  
  
  
  
  
  
