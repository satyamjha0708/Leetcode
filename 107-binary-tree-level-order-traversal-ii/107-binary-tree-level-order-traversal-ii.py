# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None: return []
        ans=[]
        queue=[]
        queue.append(root)
        
        while queue:
                size=len(queue)
                l=[]
                for i in range(size):
                        x=queue.pop(0)
                        if x.left: queue.append(x.left)
                        if x.right: queue.append(x.right)
                        l.append(x.val)
                        
                ans.append(l)
                
                
        return ans[::-1]