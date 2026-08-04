# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        res=[]
        res=[]
        if not root:
            return []
        q.append(root)
        while q:
            temp=[]
            for i in range(len(q)):

                node=q.popleft()
                # print(node.val)
                if node:
                    temp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if temp:
                res.append(temp)
        return res
        