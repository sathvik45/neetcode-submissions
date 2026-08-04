# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=float("-inf")
        def bst(root):
            nonlocal res
            if root is None:
                return 0
            # if root.val<0:
            #     return max()
            left=max(bst(root.left),0)
            right=max(bst(root.right),0)
            # temp=max(root.val,root.val + max(left,right))
            res=max(res,root.val+left+right)
            return root.val + max(left,right)
        bst(root)
        return res

        