# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        nex=None if head is None else curr.next
        while curr and nex:
            if curr.val==nex.val:
                curr.next=nex.next
            else:
                curr=nex
            nex=curr.next
        return head
    
    
    
   