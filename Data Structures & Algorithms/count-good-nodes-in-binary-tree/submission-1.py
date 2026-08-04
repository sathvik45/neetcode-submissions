# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    c=0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,m):
            if not root:
                return
            if root.val >= m:
                self.c+=1
            m=max(m,root.val)
            dfs(root.left,m)
            dfs(root.right,m)
        dfs(root,-100)
        return self.c