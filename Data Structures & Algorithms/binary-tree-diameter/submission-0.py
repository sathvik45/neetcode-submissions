# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(root):
            if not root:
                return 0
            return 1+max(height(root.left),height(root.right))
        print(height(root))
        def diameter(root):
            if not root:
                return
            temp=height(root.left)+height(root.right)
            print(temp)

            self.res=max(self.res,temp)
            print(self.res)
            diameter(root.left)
            diameter(root.right)
        diameter(root)
        return self.res


        