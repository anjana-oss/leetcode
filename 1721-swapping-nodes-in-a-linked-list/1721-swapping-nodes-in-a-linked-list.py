# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        count=0
        first=None
    

        while curr:
            count+=1
            curr=curr.next
        
        curr=head
        for _ in range(k-1):
            curr=curr.next
        first=curr


        curr=head
        pos=count-k+1
        for _ in range(pos-1):
            curr=curr.next

        first.val,curr.val=curr.val,first.val

        return head
