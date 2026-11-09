# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        vals=[]
        def dfs(node,path):
            
            if node is None:
                return 
            if node.left is None and node.right is None:
                vals.append(path)
                return
            if node.left:
                path1=path+"->"+str(node.left.val)
                dfs(node.left,path1)
            if node.right:
                path2=path+"->"+str(node.right.val)
                dfs(node.right,path2)

        if root:

            dfs(root,str(root.val))
        return vals

          