# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# find the valid node

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node=TreeNode(val)
        if not root:
            root=new_node
        def dfs(node):
            if node is None:
                return
            
            if val> node.val:
                if node.right is None:
                    node.right=TreeNode(val)
                    return
                dfs(node.right)
            if val<node.val:
                if node.left is None:
                    node.left=TreeNode(val)
                    return
                dfs(node.left)
        dfs(root)
        return root