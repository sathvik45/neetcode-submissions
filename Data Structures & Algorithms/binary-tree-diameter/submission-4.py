# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#find depths of all the nodes, then return the max of left + rifht depth
# for a node find the depth of left and right 
# and left + right into res var
# dfs for all the nodes and repeate above 2 steps

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if not node:
                return depth
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
        res = 0
        def DFS(root):
            nonlocal res
            if not root:
                return 
            left_depth = dfs(root.left, 0)
            right_depth = dfs(root.right , 0)
            res = max(left_depth + right_depth, res)
            print(res)
            DFS(root.left)
            DFS(root.right)
        DFS(root)
        return res



            
            
        