# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    store=True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            print(abs(left-right))
            if abs(left - right)>1:
                
                self.store=False
            height=1+max(left,right)
            print(left,right,height)
            # print(left,right,self.store)
            
            
            return height
        print(dfs(root))
        return self.store

        