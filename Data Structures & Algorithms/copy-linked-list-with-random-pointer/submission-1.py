"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return 
        hashmap={}
        res=Node(0)
        temp=res
        while head:
            if hashmap.get(head) is None:
                temp.val=head.val
                hashmap[head]=temp
            if head.next:
                if hashmap.get(head.next) is not None:
                    temp.next=hashmap[head.next]
                else:
                    temp.next=Node(head.next.val)
                    hashmap[head.next]=temp.next
            if head.random:
                if hashmap.get(head.random) is not None:
                    temp.random=hashmap[head.random]
                else:
                    temp.random=Node(head.random.val)
                    hashmap[head.random]=temp.random
            temp=temp.next
            head=head.next
        return res
                

        