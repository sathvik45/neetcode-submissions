# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    d={None:0}
    res=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            h = 1 + max(height(root.left),height(root.right))
            # print(h)
            self.d[root]=h
            return h
        height(root)
        # for k,v in self.d.items():
        #     print(k.val,v)


        def diameter(root):
            if not root:
                return
            self.res=max(self.res,self.d[root.left]+self.d[root.right])
            diameter(root.left)
            diameter(root.right)
        diameter(root)
        return self.res

        