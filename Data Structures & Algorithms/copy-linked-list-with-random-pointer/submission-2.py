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
        curr=head
        hm={None:None}
        while curr:
            hm[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            temp=hm[curr]
            temp.next=hm[curr.next]
            temp.random=hm[curr.random]
            curr=curr.next
        return hm[head]

        