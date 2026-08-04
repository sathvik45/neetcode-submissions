# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# instead of having 2 dfs, we can use one dfs and post order travesal
# caliculate the depth and diameter at the same time
# cal left depth and right depth
# update the res with the latest diameter and at the end return the depth
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        def dfs(node):
            if not node:
                return 0

            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)

            self.res = max(self.res, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        
        dfs(root)
        return self.res
