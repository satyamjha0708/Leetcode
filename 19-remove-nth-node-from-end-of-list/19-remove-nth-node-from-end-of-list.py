# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
                count+=1
                temp=temp.next
                
                
        l=count-n
        
        
        if l==0:
                return head.next
        
        
        temp1=head
        for i in range(1,l):
                temp1=temp1.next
                
                
        temp1.next=temp1.next.next
        
        return head