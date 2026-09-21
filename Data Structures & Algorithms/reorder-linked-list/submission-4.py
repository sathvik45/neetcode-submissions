# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow= head
        fast =head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow.next.val)
        
        cur = slow.next
        rev = slow.next = None
        while cur:
            temp = cur.next
            cur.next = rev
            rev = cur
            cur = temp
        
        while rev:
            temp1, temp2 = head.next, rev.next
            head.next = rev
            rev.next = temp1
            head,rev = temp1, temp2
        
        



        
        