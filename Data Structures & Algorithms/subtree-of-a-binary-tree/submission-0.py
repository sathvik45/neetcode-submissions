# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root,subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return sameTree(root.left,subRoot.left) and sameTree(root.right,subRoot.right)
            else:
                return False

        def dfs(root,subRoot):
            if subRoot is None:
                return True
            if root is None:
                return False
            if sameTree(root,subRoot):
                return True
            return dfs(root.left,subRoot) or dfs(root.right,subRoot)
        return dfs(root,subRoot)