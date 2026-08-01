# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=collections.deque([root])
        reverse=False

        while q:
            qlen=len(q)
            level=[]
            for i in range(qlen):
                node=q.popleft()
                

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)


            if reverse and level:
                level.reverse()
                res.append(level)
            elif level:
                res.append(level)
            reverse=not reverse
                

        return res