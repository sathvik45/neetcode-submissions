# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        q.append(root)
        res=[]
        while q:
            temp=None
            len_q=len(q)
            for _ in range(len_q):
                node=q.popleft()
                if node:
                    temp=node
                    q.append(node.left)
                    q.append(node.right)
            if temp:
                res.append(temp.val)
            
        return res
