# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=None
        slow=head
        fast=head
        
        if head.next==None:
                return None
        
        
        if head==None:
                return None
        
        while  fast and fast.next:
                temp=slow
                slow=slow.next
                fast=fast.next.next
                
                
    
        if slow.next:
                temp.next=temp.next.next
                
                
        elif slow.next==None:
                temp.next=None
                
                
        
        return head
                
                
                
        
        
        