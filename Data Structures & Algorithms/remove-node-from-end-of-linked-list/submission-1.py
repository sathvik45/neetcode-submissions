# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res=ListNode()
        res.next=head
        temp=head
        while n:
            temp=temp.next
            n-=1
        # print(temp.val)
        curr=res
        while temp:
            print(temp.val,curr.val)
            temp=temp.next
            curr=curr.next
        # print(curr.val)
        curr.next=curr.next.next
        return res.next

    