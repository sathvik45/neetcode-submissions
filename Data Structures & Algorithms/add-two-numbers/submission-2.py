# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1=''
        str2=''
        while l1:
            str1+=str(l1.val)
            l1=l1.next
        while l2:
            str2+=str(l2.val)
            l2=l2.next
        num=int(str1[::-1])+int(str2[::-1])
        # print(num)
    
        res=ListNode()
        if num==0:
            return res
        temp=res
        while num:
            temp.next=ListNode(num%10)
            num=int(num/10)
            # print(num)
            temp=temp.next
        return res.next

